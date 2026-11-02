#!/usr/bin/env python3
"""Detecção demonstrativa de 5 falhas de login em janela móvel de 5 minutos.
Dados de entrada devem ser fictícios. Usa somente a biblioteca padrão.
"""
import argparse
import csv
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from pathlib import Path

FIELDS = ('timestamp', 'source_ip', 'username', 'event_type', 'status', 'host')

def carregar_eventos(caminho):
    with caminho.open(newline='', encoding='utf-8-sig') as arquivo:
        leitor = csv.DictReader(arquivo)
        if not leitor.fieldnames or not set(FIELDS).issubset(leitor.fieldnames):
            raise ValueError(f'CSV deve conter as colunas: {", ".join(FIELDS)}')
        eventos = []
        for numero, linha in enumerate(leitor, start=2):
            try:
                instante = datetime.fromisoformat(linha['timestamp'].replace('Z', '+00:00'))
                if instante.tzinfo is None:
                    raise ValueError('fuso horário ausente')
                instante = instante.astimezone(timezone.utc)
            except (ValueError, AttributeError) as erro:
                raise ValueError(f'Timestamp inválido na linha {numero}: {erro}') from erro
            if not linha['source_ip'] or not linha['username']:
                raise ValueError(f'IP ou usuário ausente na linha {numero}')
            eventos.append((instante, linha))
    return sorted(eventos, key=lambda evento: evento[0])

def detectar(eventos, limite=5, minutos=5):
    janelas = defaultdict(deque)
    alertados = set()
    alertas = []
    for instante, evento in eventos:
        if evento['event_type'].lower() != 'login' or evento['status'].lower() != 'failure':
            continue
        chave = (evento['source_ip'], evento['username'], evento['host'])
        janela = janelas[chave]
        janela.append(instante)
        while janela and (instante - janela[0]) > timedelta(minutes=minutos):
            janela.popleft()
        if len(janela) >= limite and chave not in alertados:
            alertas.append({
                'timestamp': instante.isoformat().replace('+00:00', 'Z'),
                'rule_id': 'SOC-001', 'severity': 'medium',
                'source_ip': chave[0], 'username': chave[1], 'host': chave[2],
                'failure_count': str(len(janela)),
                'description': f'{limite} ou mais falhas de login em {minutos} minutos'
            })
            alertados.add(chave)
    return alertas

def detectar_soc002(eventos, limite=5, minutos=5):
    """Correlaciona >= limite falhas em janela móvel com sucesso posterior.

    Falhas e sucesso devem compartilhar IP, usuário e host. A janela
    termina no instante do sucesso; um alerta é gerado por sucesso elegível.
    """
    if limite <= 0 or minutos <= 0:
        raise ValueError('limite e minutos devem ser positivos')
    janelas = defaultdict(deque)
    alertas = []
    for instante, evento in sorted(eventos, key=lambda item: item[0]):
        if evento['event_type'].lower() != 'login':
            continue
        chave = (evento['source_ip'], evento['username'], evento['host'])
        janela = janelas[chave]
        while janela and instante - janela[0] > timedelta(minutes=minutos):
            janela.popleft()
        status = evento['status'].lower()
        if status == 'failure':
            janela.append(instante)
        elif status == 'success':
            if len(janela) >= limite:
                alertas.append({
                    'timestamp': instante.isoformat().replace('+00:00', 'Z'),
                    'rule_id': 'SOC-002', 'severity': 'high',
                    'source_ip': chave[0], 'username': chave[1], 'host': chave[2],
                    'failure_count': str(len(janela)),
                    'description': f'Login bem-sucedido após {len(janela)} falhas em até {minutos} minutos'
                })
            # Reinicia contagem após sucesso, inclusive quando não houve alerta.
            janela.clear()
    return alertas


def detectar_alertas(eventos, limite=5, minutos=5):
    """Executa as duas regras sem alterar a função original SOC-001."""
    eventos = list(eventos)
    return sorted(
        detectar(eventos, limite, minutos) + detectar_soc002(eventos, limite, minutos),
        key=lambda alerta: (alerta['timestamp'], alerta['rule_id'])
    )


def executar():
    raiz = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description='Analisa tentativas de login em CSV fictício')
    parser.add_argument('--input', type=Path, default=raiz / 'logs' / 'eventos-simulados.csv')
    parser.add_argument('--output', type=Path, default=raiz / 'outputs' / 'alertas.csv')
    parser.add_argument('--limite', type=int, default=5)
    parser.add_argument('--minutos', type=int, default=5)
    args = parser.parse_args()
    if args.limite <= 0 or args.minutos <= 0:
        parser.error('--limite e --minutos devem ser positivos')
    alertas = detectar_alertas(carregar_eventos(args.input), args.limite, args.minutos)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    campos = ['timestamp', 'rule_id', 'severity', 'source_ip', 'username', 'host', 'failure_count', 'description']
    with args.output.open('w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(alertas)
    print(f'Análise concluída: {len(alertas)} alerta(s). Saída: {args.output}')

if __name__ == '__main__':
    executar()
