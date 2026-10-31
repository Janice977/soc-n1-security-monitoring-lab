# INC-001 — Tentativas repetidas de autenticação (simulação)

**Natureza:** exercício fictício; nenhum incidente real foi investigado.

| Campo | Valor |
|---|---|
| Evento | SOC-001 — 5 falhas em 5 minutos |
| Data/hora de detecção | 2026-10-20 09:01:00 UTC |
| IP de origem | 198.51.100.23 (bloco reservado para documentação) |
| Usuário / host | admin / web-01 |
| Severidade inicial | Média, sujeita à triagem |
| Status | Pendente de verificação contextual (simulado) |

## Evidências do conjunto fictício

Cinco falhas de login ocorreram entre 09:00 e 09:01 UTC, seguidas de uma autenticação bem-sucedida às 09:02 UTC. O script detecta as falhas; a correlação com o sucesso é feita **manualmente** neste relatório, não pela regra automatizada.

## Hipóteses e validações

- Hipótese: possível tentativa de adivinhação de senha. Não é possível confirmar comprometimento apenas com esses dados.
- Verificar autorização da atividade, origem esperada, logs complementares e eventual MFA em ambiente real.
- Em ambiente real, considerar escalonamento imediato quando houver acesso confirmado não autorizado.

## Ações propostas (não executadas)

Abrir ticket, preservar evidências, investigar sucesso de autenticação, aplicar procedimentos aprovados de contenção e escalar para SOC N2 conforme criticidade.

## Conclusão

Evento suspeito demonstrativo que precisa de triagem. O exemplo não comprova ataque ou vazamento.
