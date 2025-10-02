#########################################################################################
#
# git remote add origin https://github.com/AnaPaulistaGit/PerformanceCarteira.git 🚀 👀 💥😱 🔵 🌟
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


# 👉 Função para carregar dados (com tratamento para 1 ticker vs vários)
@st.cache_data(show_spinner=False)
def carregar_dados(empresas):
    cotacoes = yf.download(
        empresas,
        start="2020-01-01",
        end="2026-01-01",
        auto_adjust=True,
        threads=True
    )

    # Se for apenas um ticker → colunas simples
    if isinstance(cotacoes.columns, pd.MultiIndex):
        cotacoes = cotacoes["Close"]
    else:
        cotacoes = cotacoes[["Close"]]
    return cotacoes


@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv(r'C:\Ana\GitHub\PerformanceCarteira\IBOV.csv', sep=';')              
    tickers = [f"{codigo}.SA" for codigo in base_tickers["Codigo"]]
    return tickers


# 👉 Exibe mensagem de carregamento enquanto busca os dados 
with st.spinner("Aguarde enquanto os dados são carregados..."):
    acoes = carregar_tickers_acoes()
    dados = carregar_dados(acoes)


# 👉 Interface do aplicativo
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos
""")

st.sidebar.header("Filtros")

# 👉 filtro de ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

if not dados.empty:
    # filtro de datas
    data_inicial = dados.index.min().to_pydatetime()
    data_final = dados.index.max().to_pydatetime()

    intervalo_data = st.sidebar.slider(
        "Selecione o período", 
        min_value=data_inicial, 
        max_value=data_final,
        value=(data_inicial, data_final),
        step=timedelta(days=1)
    )

    # aplica o filtro de datas
    dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

    # 👉 cria o gráfico
    st.line_chart(dados)

    # 👉 cálculo de performance
    if len(lista_acoes) == 0:
        lista_acoes = list(dados.columns)
    elif len(lista_acoes) == 1:
        dados = dados.rename(columns={"Close": acao_unica})

    # 👉 performance por ativo (vetorizado)
    inicio = dados.iloc[0]
    fim = dados.iloc[-1]
    performance = (fim / inicio - 1).astype(float)

    texto_performance_ativos = ""
    carteira_inicial = 1000 * len(lista_acoes)
    carteira_final = 0

    for acao, perf in performance.items():
        if pd.isna(perf):
            texto_performance_ativos += f"  \n{acao}: :orange[sem dados suficientes para cálculo]"
            continue

        carteira_final += 1000 * (1 + perf)

        if perf > 0:
            texto_performance_ativos += f"  \n{acao}: :green[{perf:.1%}]"
        elif perf < 0:
            texto_performance_ativos += f"  \n{acao}: :red[{perf:.1%}]"
        else:
            texto_performance_ativos += f"  \n{acao}: {perf:.1%}"

    performance_carteira = carteira_final / carteira_inicial - 1

    if performance_carteira > 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
    elif performance_carteira < 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
    else:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"

    st.subheader("Performance dos Ativos")
    st.write("Essa foi a performance de cada ativo no período selecionado:")

    st.markdown(texto_performance_ativos)
    st.markdown(texto_performance_carteira)

else:
    st.warning("Nenhum dado disponível para as ações selecionadas.")

