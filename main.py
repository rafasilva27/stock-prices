import math
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta

st.write("""# App Preço de Ações""")

@st.cache_data # pra armazenar os dados em cache
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2009-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"]) # pegando apenas a coluna Código
    tickers = [item + ".SA" for item in tickers] # adicionando .SA no final de cada ticker
    return tickers

acoes = carregar_tickers_acoes()
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
intervalo_data = st.sidebar.slider("Selecione o periodo:", min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final), step=timedelta(days=1), format="DD/MM/YY")

dados = dados.loc[intervalo_data[0]:intervalo_data[1]] # filtrando as linhas que correspondem ao intervalo de datas selecionado pelo usuário        
        
st.line_chart(dados) # criando o gráfico

texto_performance_ativos = " "

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={"Close": acao_unica})

for acao in lista_acoes:
    performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1 # calculando a performance de quantos % cada ativo subiu ou caiu no período, valor final / valor inicial - 1
    performance_ativo = float(performance_ativo)
    
    if performance_ativo > 0:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativo:.1%}]"
    elif performance_ativo < 0:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativo:.1%}]"
    elif math.isnan(performance_ativo):
        texto_performance_ativos = texto_performance_ativos +  f"  \n{acao}: :blue[-]"    

st.write(f"""
Essa foi a performance de cada ativo no período selecionado:
   {texto_performance_ativos}     
""")