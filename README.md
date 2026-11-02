#  SOC N1 — Security Monitoring Lab

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white) ![SOC](https://img.shields.io/badge/SOC-N1-1F2937) ![Blue Team](https://img.shields.io/badge/Blue_Team-Laborat%C3%B3rio-2563EB) ![Dados](https://img.shields.io/badge/Dados-Simulados-0F766E)

**Laboratório educacional de monitoramento de eventos de autenticação, detecção de padrões suspeitos e triagem inicial de alertas, desenvolvido em Python.**

> **Escopo:** projeto de portfólio com dados fictícios. Não representa atuação em um SOC de produção, detecção validada em ambiente real ou integração com plataformas SIEM/EDR.

##  Objetivo

Exercitar atividades introdutórias de **Analista de Segurança da Informação / SOC N1**, incluindo:

- Leitura e organização de logs de autenticação;
- Identificação de eventos repetitivos em uma janela temporal;
- Geração e interpretação de alerta;
- Registro de evidências e hipóteses de análise;
- Documentação de incidente simulado e critérios de escalonamento.

##  Cenário de detecção

O script lê os eventos em `logs/eventos-simulados.csv`, ordena-os pelo horário e procura **cinco falhas de login em cinco minutos** para a mesma combinação de **IP de origem, usuário e host**.

Quando a condição é satisfeita, é gerado o alerta **SOC-001** em `outputs/alertas.csv`. A regra foi desenhada para gerar apenas o primeiro alerta por combinação IP/usuário/host em cada execução.

A regra **SOC-002** correlaciona as mesmas cinco falhas com um **login bem-sucedido dentro de cinco minutos**, para o mesmo IP, usuário e host. A janela se reinicia após o sucesso. O cenário fictício original contém ambas as ocorrências.

| Item | Exemplo documentado |
| --- | --- |
| Tipo de evento | Falhas repetidas de autenticação |
| Regra | 5 falhas em 5 minutos |
| IP de origem | `198.51.100.23` |
| Usuário | `admin` |
| Host | `web-01` |
| Saída esperada para os dados de exemplo | 2 alertas: `SOC-001` e `SOC-002` |

O endereço IP pertence a uma faixa reservada para documentação (RFC 5737). O exemplo **não contém IP ou credenciais de usuários reais**.

##  Como reproduzir o laboratório

**Requisito:** Python 3.9 ou superior, sem dependências adicionais.

1. Baixe o repositório ou clone-o localmente.
2. Abra um terminal na pasta principal do projeto.
3. Execute a análise e os testes:

```bash
python scripts/analisar_logs.py
python -m unittest discover -s tests -v
```

**Windows:** se o comando `python` não funcionar, tente o inicializador `py` (caso esteja instalado):

```powershell
py scripts/analisar_logs.py
py -m unittest discover -s tests -v
```

Consulte o arquivo `outputs/alertas.csv` para verificar a saída. O exemplo do projeto documenta a geração de **dois alertas** para o cenário simulado. Esse resultado foi confirmado nos testes locais.

##  Estrutura

```text
soc-n1-security-monitoring-lab/
├── README.md
├── logs/
│   └── eventos-simulados.csv
├── scripts/
│   └── analisar_logs.py
├── deteccoes/
│   └── regras-de-deteccao.md
├── incidentes/
│   ├── relatorio-incidente-001.md
│   └── relatorio-incidente-002.md
├── docs/
│   └── guia-de-uso.md
├── tests/
│   └── test_analisar_logs.py
└── outputs/
    └── alertas.csv
```

##  Fluxo de triagem SOC N1

1. **Coleta:** interpretar os eventos fictícios de autenticação.
2. **Detecção:** verificar padrões de falhas repetidas para IP, usuário e host.
3. **Validação:** conferir horários, agrupamento e contexto do alerta.
4. **Investigação preliminar:** considerar hipóteses legítimas (por exemplo, erro de senha) e suspeitas; verificar manualmente se há sucesso posterior.
5. **Registro:** documentar evidências, limitações e ações recomendadas no relatório simulado.
6. **Escalonamento:** indicar quando seria necessária uma análise adicional, sem agir sobre sistemas reais.

**Documentação relacionada:**

- [Guia de uso](docs/guia-de-uso.md)
- [Regra de detecção](deteccoes/regras-de-deteccao.md)
- [Relatório SOC-001](incidentes/relatorio-incidente-001.md)
- [Relatório SOC-002](incidentes/relatorio-incidente-002.md)
- [Logs fictícios](logs/eventos-simulados.csv)

##  Competências demonstradas pelo projeto

| Área | Evidência no repositório |
| --- | --- |
| Análise inicial de logs | Conjunto fictício de autenticações em CSV |
| Detecção por regra | Script Python e especificação de regra |
| Triagem e documentação | Relatório de incidente simulado |
| Testes de software | Testes com `unittest` |
| Organização técnica | Separação de scripts, documentação, logs e saídas |

##  Limitações

Falhas repetidas **não comprovam ataque**, e a regra pode produzir falsos positivos. Este protótipo não detecta tentativas distribuídas, não confirma comprometimento e não se conecta a SIEM, EDR ou sistemas reais. O relatório de incidente representa uma **simulação educacional**, não um incidente investigado profissionalmente.

##  Próximas melhorias planejadas

- Refinar a correlação dos alertas SOC-001 e SOC-002 e suas hipóteses de falsos positivos;
- Criar métricas simples e gráficos locais a partir dos dados simulados;
- Adicionar exemplos documentados de falsos positivos e critérios de escalonamento;
- Experimentar uma ferramenta gratuita de monitoramento **somente em laboratório isolado e autorizado**.

##  Autoria e portfólio

Projeto de aprendizagem e evolução profissional de **Janice Lira**, voltado ao desenvolvimento de competências introdutórias em Segurança da Informação e SOC N1.

- [Perfil GitHub](https://github.com/Janice977)
- [LinkedIn](https://www.linkedin.com/in/janicelira)

---

**Uso educacional:** todos os dados de exemplo são fictícios. Não realizar testes em serviços ou sistemas de terceiros sem autorização.
