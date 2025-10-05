#########################################################################################
#
# Performance Carteira - Dashboard de Açoes 🚀 👀 💥😱 🔵 🌟
# https://github.com/AnaPaulistaGit/PerformanceCarteira.git 
#
# Nesse projeto vamos construir um aplicativo que mostra a evoluçao dos preços das
# das principais açoes negociadas no IBOVESPA ao longo dos anos.
# Para o desenvolvimento do app vamos utilizar o Streamlit, uma importante biblioteca
# python de codigo aberto que permite criar e partilhar aplicaçoes web para ciencia de 
# dados e machine learning de forma rapida e facil.
#
# Biblioteca que serão usadas: 👇
# • Streamlit
# • pandas
# • datetime
# • ferramentas auxiliares: yfinance (usar o comando pip install)
#
# Entendendo decorator 💡
# O decorator adiciona uma nova funcionalidade a funçao sem mudar o seu codigo original
# ou seja adiciona uma logica extra antes ou depois da execuçao da funçao original, e 
# então retorna uma nova funçao "envelopada". Sua sintaxe é representada pelo simbolo @
#
#
# Entendendo config.toml 💡
# O config.toml é um arquivo de configuração que usa o formato TOML, projetado para 
# tornar a configuração de um programa mais organizada, legível e fácil de editar sem
# alterar o codigo fonte do aplicativo. O Streamlit executa o arquivo config.toml buscando-o
# dentro da pasta .Streamlit
# 
#
#
#########################################################################################
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

# Função para carregar dados das ações
@st.cache_data
def carregar_dados(empresas):
    cotacoes = yf.download(empresas, start="2020-01-01", end="2026-01-01", auto_adjust=True)
    # Garante que existe a coluna "Close" (quando há apenas uma ação, o DataFrame é diferente)
    if "Close" in cotacoes:
        cotacoes = cotacoes["Close"]
    else:
        cotacoes = cotacoes
    return cotacoes

# Função para carregar tickers das ações do IBOV
@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv(r'IBOV.csv', sep=';')              
    tickers = [item + ".SA" for item in base_tickers["Codigo"]]
    return tickers

# Interface do Streamlit
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos
""")

# Exibe mensagem de carregamento enquanto dados são baixados
with st.spinner("Aguarde enquanto os dados são carregados..."):
    acoes = carregar_tickers_acoes()
    dados = carregar_dados(acoes)

# Painel lateral (sidebar)
st.sidebar.header("Filtros")

# Filtro de ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

if not dados.empty:
    # Filtro de datas
    data_inicial = dados.index.min().to_pydatetime()
    data_final = dados.index.max().to_pydatetime()
    intervalo_data = st.sidebar.slider(
        "Selecione o período",
        min_value=data_inicial,
        max_value=data_final,
        value=(data_inicial, data_final),
        step=timedelta(days=1)
    )

    # Filtra os dados pelo período selecionado
    dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

    # Cria o gráfico
    st.line_chart(dados)

    # Cálculo de performance
    texto_performance_ativos = ""

    if len(lista_acoes) == 0:
        lista_acoes = list(dados.columns)
    elif len(lista_acoes) == 1:
        dados = dados.rename(columns={"Close": acao_unica})

    carteira = [1000 for _ in lista_acoes]
    total_inicial_carteira = sum(carteira)

    acoes_validas = []
    for i, acao in enumerate(lista_acoes):
        # Verifica se há dados válidos no início e fim do período
        if pd.isna(dados[acao].iloc[0]) or pd.isna(dados[acao].iloc[-1]):
            texto_performance_ativos += f"  \n{acao}: :orange[sem dados suficientes para cálculo]"
            continue

        performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
        performance_ativo = float(performance_ativo)
        carteira[i] *= (1 + performance_ativo)
        acoes_validas.append(i)

        if performance_ativo > 0:
            texto_performance_ativos += f"  \n{acao}: :green[{performance_ativo:.1%}]"
        elif performance_ativo < 0:
            texto_performance_ativos += f"  \n{acao}: :red[{performance_ativo:.1%}]"
        else:
            texto_performance_ativos += f"  \n{acao}: {performance_ativo:.1%}"

    total_final_carteira = sum([carteira[i] for i in acoes_validas])
    performance_carteira = total_final_carteira / total_inicial_carteira - 1

    if performance_carteira > 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
    elif performance_carteira < 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
    else:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"

    # Exibe performance com o período selecionado formatado
    st.subheader("Performance dos Ativos")
    st.write(f"Essa foi a performance de cada ativo no período selecionado: **{intervalo_data[0].strftime('%d/%m/%Y')} a {intervalo_data[1].strftime('%d/%m/%Y')}**")

    st.markdown(texto_performance_ativos)
    st.markdown(texto_performance_carteira)

else:
    st.warning("Nenhum dado disponível para as ações selecionadas.")
    
