import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analisar_logs import carregar_eventos, detectar

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

if __name__ == '__main__':
    unittest.main()
