# Regras de detecção (exemplos didáticos)

## SOC-001 — Falhas repetidas de autenticação

- **Condição implementada:** pelo menos 5 falhas de login para a mesma combinação `source_ip`, `username` e `host` dentro de 5 minutos (janela móvel).
- **Severidade inicial:** média; requer validação contextual por analista.
- **Evidência mínima:** IP de origem, usuário, host, horário UTC e número de tentativas.
- **Ação SOC N1:** verificar origem e atividade legítima, correlacionar com sucesso posterior e histórico; abrir ticket e escalar conforme procedimento da organização.
- **Falsos positivos possíveis:** erro de senha repetido por usuário legítimo ou automação mal configurada.
- **Limitações:** uso de dados simulados; não detecta ataques distribuídos entre IPs/usuários, nem agrega sucessos; aplica supressão de alertas repetidos por chave durante toda a execução.

**Nota:** regra didática; não é uma assinatura validada para ambiente de produção.


## SOC-002 — Sucesso após falhas repetidas

- **Condição implementada:** pelo menos 5 falhas de login nos 5 minutos anteriores a um login bem-sucedido, com mesma combinação `source_ip`, `username` e `host`. A borda de 5 minutos está incluída.
- **Severidade inicial:** alta, apenas para priorização didática; **não comprova invasão**.
- **Evidência mínima:** IP, usuário, host, horário UTC do sucesso e quantidade de falhas na janela.
- **Ação SOC N1:** confirmar autorização do acesso, analisar atividades subsequentes e registrar hipótese; escalar conforme procedimento simulado.
- **Falsos positivos:** usuário legítimo que digitou senha incorreta e depois acertou.
- **Limitações:** a janela é reiniciada em cada sucesso; não há correlação distribuída nem reputação de IP. Um alerta é emitido por sucesso elegível.
- **Exemplo fictício:** cinco falhas para `admin` em `web-01` pelo IP `198.51.100.23`, seguidas de sucesso às `09:02:00Z` no mesmo dia.

Esta regra é educacional e não está validada para monitoramento em produção.
