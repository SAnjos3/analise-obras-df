# Análise de Obras do Distrito Federal

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A transparência e a governança na aplicação de recursos públicos são pilares fundamentais para a gestão pública e o controle social. Nesse contexto, o Governo Federal instituiu o ObrasGov.br, uma plataforma tecnológica destinada a centralizar, monitorar e dar publicidade aos investimentos federais em infraestrutura. A plataforma visa atender às demandas da sociedade e de órgãos de controle, como o Tribunal de Contas da União (TCU), por informações claras, atualizadas e que permitam o acompanhamento efetivo das políticas públicas.

Este projeto, desenvolvido como parte de um processo seletivo, propõe um ciclo completo de análise de dados focado nos projetos de investimento do Distrito Federal registrados nesta plataforma. Embora o cadastro de projetos com recursos próprios por parte do DF seja facultativo, a análise dos dados federais e locais registrados oferece um panorama crucial sobre os investimentos na capital.

Seguindo uma metodologia estruturada, este notebook documenta todas as etapas do processo:

- Extração (ETL): Coleta dos dados brutos diretamente da API pública do ObrasGov.br.

- Análise Exploratória (EDA): Investigação da qualidade, formato e estrutura dos dados, baseada nas métricas de qualidade da IBM.

- Tratamento e Normalização: Limpeza, correção de inconsistências e transformação de dados complexos (JSON) em um esquema relacional.

- Armazenamento: Persistência dos dados tratados em um banco de dados relacional (SQLite) com integridade referencial.

- Análise e Visualização: Geração de análises quantitativas e qualitativas para extrair insights sobre o perfil, tendências e características das obras no DF.

O objetivo final é demonstrar as capacidades técnicas de manipulação e análise de dados, ao mesmo tempo em que se produz uma avaliação concreta sobre a qualidade dos dados de transparência e os padrões de investimento refletidos na base do ObrasGov.br.

API:
https://api.obrasgov.gestao.gov.br/obrasgov/api/swagger-ui/index.html#/

## Project Organization

```
├── analise_obras_df
│   ├──__init__.py
│   └──  analise.py
├── data
│   ├── 1-raw
│   └── 2-processed
├── references
│   
├── reports
│   └──  1.0-extracao_e_analise.html
├── LICENSE
├── Makefile
├── notebooks
│   └── 1.0-extracao_e_analise.ipynb
├── pyproject.toml
├── README.md

│   └── figures
└── requirements.txt

11 directories, 11 files
```

--------


## Referências Bibliográficas
BRASIL. Ministério da Gestão e da Inovação em Serviços Públicos. ObrasGov.br API: Swagger UI. [S.l.], [20--?]. Disponível em: https://api.obrasgov.gestao.gov.br/obrasgov/api/swagger-ui/index.html#/Projeto%20De%20Investimento/buscarPorFiltro. Acesso em: 17 out. 2025.

CONVERT columns to string in pandas. Stack Overflow, 13 mar. 2014. Disponível em: https://stackoverflow.com/questions/22005911/convert-columns-to-string-in-pandas. Acesso em: 17 out. 2025.

DATASCIENCE-PM.COM. CRISP-DM for Data Science 2025. [S.l.]: DataScience-PM.com, 2024. Disponível em: https://www.datascience-pm.com/wp-content/uploads/2024/12/CRISP-DM-for-Data-Science-2025.pdf. Acesso em: 17 out. 2025.

IBM. Modeler CRISP-DM Guide. [S.l.]: IBM, [20--?]. Disponível em: https://www.ibm.com/docs/pt-br/SS3RA7_18.5.0/nl/pt/BR/pdf/ModelerCRISPDM.pdf. Acesso em: 17 out. 2025.

IBM. Métricas de qualidade de dados: o que são e por que são importantes. [S.l.]: IBM, [20--?]. Disponível em: https://www.ibm.com/br-pt/think/insights/data-quality-metrics. Acesso em: 17 out. 2025.

IBM. What is exploratory data analysis? [S.l.]: IBM, [20--?]. Disponível em: https://www.ibm.com/think/topics/exploratory-data-analysis. Acesso em: 17 out. 2025.

KNAFLIC, Cole Nussbaumer. Storytelling with data. [S.l.: s.n.], 2022. Disponível em: https://s3.amazonaws.com/files.commons.gc.cuny.edu/wp-content/blogs.dir/20521/files/2022/09/Knaflic-storytelling-data.pdf. Acesso em: 17 out. 2025.

PYDATA. Getting started - Overview: pandas documentation. [S.l.]: PyData, [20--?]. Disponível em: https://pandas.pydata.org/docs/getting_started/overview.html. Acesso em: 17 out. 2025.

REQUESTS: HTTP for Humans™. [S.l.]: Read the Docs, [20--?]. Disponível em: https://requests.readthedocs.io/en/latest/. Acesso em: 17 out. 2025.