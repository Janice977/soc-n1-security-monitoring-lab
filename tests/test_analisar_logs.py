import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analisar_logs import carregar_eventos, detectar, detectar_soc002, detectar_alertas

class TesteDeteccao(unittest.TestCase):
    def test_exemplo_dispara_um_alerta(self):
        raiz = Path(__file__).resolve().parents[1]
        alertas = detectar(carregar_eventos(raiz / 'logs' / 'eventos-simulados.csv'))
        self.assertEqual(len(alertas), 1)
        self.assertEqual(alertas[0]['source_ip'], '198.51.100.23')
        self.assertEqual(alertas[0]['failure_count'], '5')

    def test_falhas_esparsas_nao_disparam(self):
        inicio = datetime(2026, 10, 20, tzinfo=timezone.utc)
        eventos = [(inicio + timedelta(minutes=i*10), {'source_ip':'192.0.2.2','username':'teste','host':'web','event_type':'login','status':'failure'}) for i in range(5)]
        self.assertEqual(detectar(eventos), [])


class TesteSOC002(unittest.TestCase):
    def setUp(self):
        self.inicio = datetime(2026, 10, 20, tzinfo=timezone.utc)

    def evento(self, minuto, status, ip='198.51.100.23', usuario='admin', host='web-01'):
        return (self.inicio + timedelta(minutes=minuto), {
            'source_ip': ip, 'username': usuario, 'host': host,
            'event_type': 'login', 'status': status
        })

    def test_exemplo_original_gera_soc001_e_soc002(self):
        raiz = Path(__file__).resolve().parents[1]
        alertas = detectar_alertas(carregar_eventos(raiz / 'logs' / 'eventos-simulados.csv'))
        self.assertEqual([a['rule_id'] for a in alertas], ['SOC-001', 'SOC-002'])
        self.assertEqual(alertas[1]['timestamp'], '2026-10-20T09:02:00Z')
        self.assertEqual(alertas[1]['failure_count'], '5')

    def test_quatro_falhas_nao_disparam(self):
        eventos = [self.evento(i * .5, 'failure') for i in range(4)]
        eventos.append(self.evento(3, 'success'))
        self.assertEqual(detectar_soc002(eventos), [])

    def test_sucesso_fora_da_janela_nao_dispara(self):
        eventos = [self.evento(i / 10, 'failure') for i in range(5)]
        eventos.append(self.evento(7, 'success'))
        self.assertEqual(detectar_soc002(eventos), [])

    def test_chaves_diferentes_nao_se_misturam(self):
        eventos = [self.evento(i / 10, 'failure') for i in range(5)]
        eventos += [self.evento(1, 'success', ip='203.0.113.9'),
                    self.evento(1.2, 'success', usuario='outro'),
                    self.evento(1.3, 'success', host='web-02')]
        self.assertEqual(detectar_soc002(eventos), [])

    def test_um_sucesso_reseta_janela(self):
        eventos = [self.evento(i / 10, 'failure') for i in range(5)]
        eventos.extend([self.evento(1, 'success'), self.evento(2, 'success')])
        self.assertEqual(len(detectar_soc002(eventos)), 1)

    def test_sucesso_antes_das_falhas_nao_dispara(self):
        eventos = [self.evento(0, 'success')]
        eventos.extend(self.evento(i + 1, 'failure') for i in range(5))
        self.assertEqual(detectar_soc002(eventos), [])

    def test_cinco_falhas_sem_sucesso_nao_disparam_soc002(self):
        eventos = [self.evento(i / 10, 'failure') for i in range(5)]
        self.assertEqual(detectar_soc002(eventos), [])

    def test_limite_da_janela_inclusivo(self):
        eventos = [self.evento(i / 10, 'failure') for i in range(5)]
        eventos.append(self.evento(5, 'success'))
        self.assertEqual(len(detectar_soc002(eventos)), 1)

if __name__ == '__main__':
    unittest.main()
