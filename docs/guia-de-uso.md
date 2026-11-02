# Guia de uso

1. Instale Python 3.9 ou superior (nenhuma dependência externa).
2. Baixe ou clone o repositório; abra um terminal na pasta do projeto.
3. Execute `python scripts/analisar_logs.py` (no Windows também pode usar `py scripts/analisar_logs.py`).
4. Leia o resultado em `outputs/alertas.csv`.
5. Execute testes: `python -m unittest discover -s tests -v`.
6. Confira a regra `deteccoes/regras-de-deteccao.md` e o relatório `incidentes/relatorio-incidente-001.md`.

**Uso responsável:** somente dados sintéticos. Não envie logs reais, credenciais, IPs identificáveis ou informações pessoais para este repositório público.

Para experimentar, altere o número de falhas com `--limite 3` ou a janela com `--minutos 10` e compare os resultados. Os resultados não substituem soluções de SIEM ou análise profissional.


## Atualização: duas regras

O comando principal agora exporta os alertas **SOC-001** e **SOC-002** para o mesmo `outputs/alertas.csv`.
O conjunto de logs fictícios incluído gera dois alertas. Execute os testes com `python -m unittest discover -s tests -v` (Windows: `py -m unittest discover -s tests -v`).
