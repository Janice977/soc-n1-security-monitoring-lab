# Relatório SOC-002 — Simulação educacional

**Classificação:** autenticação bem-sucedida após falhas repetidas (suspeita; não confirmação de ataque).

**Fonte:** `logs/eventos-simulados.csv` (dados fictícios).

**Observação dos eventos:** em 20/10/2026, cinco falhas de `admin` em `web-01` a partir de `198.51.100.23` entre 09:00 e 09:01 UTC; um sucesso correspondente às 09:02 UTC.

**Regra correlacionada:** SOC-001 (falhas repetidas) e SOC-002 (sucesso posterior dentro de cinco minutos).

**Hipóteses:** erro legítimo de senha seguido de autenticação correta; ou tentativa de acesso indevido. Os logs disponíveis não distinguem as hipóteses.

**Triagem sugerida:** verificar autorização, origem e contexto do acesso; inspecionar registros posteriores, caso existam, e escalar segundo os procedimentos da organização. Nenhuma ação real foi executada.

**Limitação:** não existem evidências de comprometimento, apenas eventos simulados.
