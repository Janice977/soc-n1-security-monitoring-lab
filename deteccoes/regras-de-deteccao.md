# Regras de detecção (exemplos didáticos)

## SOC-001 — Falhas repetidas de autenticação

- **Condição implementada:** pelo menos 5 falhas de login para a mesma combinação `source_ip`, `username` e `host` dentro de 5 minutos (janela móvel).
- **Severidade inicial:** média; requer validação contextual por analista.
- **Evidência mínima:** IP de origem, usuário, host, horário UTC e número de tentativas.
- **Ação SOC N1:** verificar origem e atividade legítima, correlacionar com sucesso posterior e histórico; abrir ticket e escalar conforme procedimento da organização.
- **Falsos positivos possíveis:** erro de senha repetido por usuário legítimo ou automação mal configurada.
- **Limitações:** uso de dados simulados; não detecta ataques distribuídos entre IPs/usuários, nem agrega sucessos; aplica supressão de alertas repetidos por chave durante toda a execução.

**Nota:** regra didática; não é uma assinatura validada para ambiente de produção.
