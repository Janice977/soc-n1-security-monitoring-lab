# SOC N1 — Security Monitoring Lab

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Status](https://img.shields.io/badge/Status-Laborat%C3%B3rio%20educacional-informational)

**Laboratório prático e reproduzível de triagem de alertas de autenticação usando Python e logs fictícios.**

## Objetivo

Demonstrar habilidades introdutórias de um SOC N1: leitura de eventos, identificação de padrões suspeitos, registro de evidências, avaliação preliminar de risco e preparação de escalonamento. **Não representa atuação em SOC real nem detecção validada para produção.**

## Funcionamento

O script analisa um CSV de autenticações e gera um alerta **SOC-001** quando encontra **cinco falhas de login em cinco minutos** para um mesmo IP de origem, usuário e host. Os registros são ordenados por timestamp, e o resultado vai para `outputs/alertas.csv`. A regra gera somente o primeiro alerta por combinação IP/usuário/host em cada execução para evitar repetições.

O conjunto de exemplo foi preparado com endereços IP reservados para documentação (RFC 5737). **Não são dados reais**.

## Comece em 2 passos

Requisitos: Python 3.9+ (sem pacotes adicionais).

```bash
python scripts/analisar_logs.py
python -m unittest discover -s tests -v
```

Saída esperada do exemplo: **1 alerta**, envolvendo o IP `198.51.100.23`, usuário `admin` e host `web-01`. Leia `outputs/alertas.csv` após executar o script.

## Estrutura

```text
soc-n1-security-monitoring-lab/
├── README.md
├── logs/eventos-simulados.csv
├── scripts/analisar_logs.py
├── deteccoes/regras-de-deteccao.md
├── incidentes/relatorio-incidente-001.md
├── docs/guia-de-uso.md
├── tests/test_analisar_logs.py
└── outputs/alertas.csv
```

## Metodologia e limitações

1. **Coleta demonstrativa:** eventos de autenticação criados para o projeto.
2. **Detecção:** falhas repetidas em janela temporal móvel, agrupadas por IP, usuário e host.
3. **Triagem:** leitura do alerta, checagem contextual e correlação manual com sucesso posterior.
4. **Documentação:** relatório fictício INC-001 com evidências e hipóteses.
5. **Escalonamento:** somente recomendações, sem ações em sistemas reais.

Falsos positivos são possíveis; falhas repetidas não provam tentativa maliciosa. A regra não identifica ataque distribuído, não infere comprometimento e não se integra a SIEM, EDR ou redes reais.

## Para explorar

- [Guia de uso](docs/guia-de-uso.md)
- [Regra de detecção](deteccoes/regras-de-deteccao.md)
- [Incidente simulado](incidentes/relatorio-incidente-001.md)
- [Logs de exemplo](logs/eventos-simulados.csv)

## Próximas melhorias

- Criar regras adicionais com testes (por exemplo, autenticação fora do horário esperado com contexto explícito).
- Incluir métricas e gráficos locais com dados sintéticos.
- Evoluir para ferramentas gratuitas de monitoramento somente em laboratório isolado e autorizado.

## Aviso

Projeto educacional de portfólio, com dados inteiramente fictícios. Não execute testes em sistemas de terceiros sem autorização. Não há dados pessoais reais no conjunto de exemplo.
