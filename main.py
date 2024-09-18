# app resultado de ações
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""")

@st.cache_data # pra armazenar os dados em cache
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2009-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "ABEV3.SA", "GGBR4.SA"]
dados  = carregar_dados(acoes) 

st.sidebar.header("Filtros")
# filtro de ações
lista_acoes = st.sidebar.multiselect("Selecione as ações que deseja visualizar:", dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})
        
# filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Selecione o periodo:", min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final), step=timedelta(days=1))

dados = dados.loc[intervalo_data[0]:intervalo_data[1]] #filtrando as linhas que correspondem ao intervalo de datas selecionado pelo usuário        
        
st.line_chart(dados)

