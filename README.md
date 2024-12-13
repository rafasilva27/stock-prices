# Aplicativo de Análise de Preços de Ações

## Descrição
Este é um aplicativo web desenvolvido em Streamlit para análise e visualização de preços de ações do mercado brasileiro (B3). A aplicação permite aos usuários explorar e comparar o desempenho de diferentes ativos ao longo do tempo.

## Funcionalidades Principais

- Carregamento automático de tickers de ações do IBOV
- Visualização de gráfico de linha com cotações históricas
- Filtros interativos para:

Seleção múltipla de ações
Intervalo de datas personalizável

- Cálculo e exibição da performance percentual de cada ativo

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) - Linguagem base

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) - Responsável pela criação da interface web interativa, com sidebar, gráficos e componentes de seleção

![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) - Manipulação e tratamento de dados

## Como Executar

Instale as dependências:
`pip install streamlit yfinance pandas`

Tenha o arquivo IBOV.csv na mesma pasta do script

Execute `streamlit run main.py`

## Observações

Dados históricos de 2009 a 2024
Performance colorida (verde para alta, vermelho para baixa)
Cache de dados para melhor performance