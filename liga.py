import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import tradingcomdados
from tradingcomdados import alternative_data as ad

# Título da página
st.title('Liga de Investimentos da UFRN')
st.markdown("[Linkedin](https://www.linkedin.com/company/ufrnliga/)")
st.markdown("[Instagram](https://www.instagram.com/ufrnliga/)")
st.markdown('---')
# Opções na barra lateral
st.sidebar.header('Estudos')
opcao_grafico = st.sidebar.radio('', ['Figuras do Ibovespa','Volatilidades no Ibovespa'])

# Se a opção "Gráfico" estiver selecionada, plote o gráfico
if opcao_grafico == 'Figuras do Ibovespa':
    st.subheader('Figuras do Ibovespa')
    st.markdown("""Atualizado diariamente.""")
    st.markdown('---')
    
    # data
    start = "2007-01-01"
    ibov = yf.download('^BVSP', start = start)['Adj Close']
    usdbrl = yf.download('USDBRL=X', start = start)['Adj Close'] 

    # dataframe
    ibovdf = pd.DataFrame(ibov)
    ibovdf.columns = ['IBOV']
    usdbrldf = pd.DataFrame(usdbrl)
    usdbrldf.columns = ['USDBRL']
    ibovusd = pd.merge(ibovdf, usdbrldf, left_index = True, right_index = True, how = 'inner')

    # dolarizando o ibov
    ibovusd['IBOVUSD'] = ibovusd['IBOV'] / ibovusd['USDBRL']

    # Plotar o gráfico do IBOV
    plt.plot(ibovusd['IBOV'], color='blue')
    plt.xlabel('Ano')
    plt.ylabel('Ibovespa')
    plt.title('Ibovespa desde 2007')
    st.pyplot(plt)

    # Plotar o gráfico do IBOVUSD
    plt.figure()
    plt.plot(ibovusd['IBOVUSD'], color='green')
    plt.xlabel('Ano')
    plt.ylabel('Ibovespa dolarizado')
    plt.title('Ibovespa dolarizado desde 2007')
    st.pyplot(plt)

if opcao_grafico == 'Volatilidades no Ibovespa':
    st.subheader('Volatilidades no Ibovespa')
    st.markdown("""Atualizado diariamente.""")
    st.markdown('---')
    
    ad.index_composition('ibov')
    codigos = ad.index_composition('ibov')['cod']
    codsa = codigos + '.SA'
    # Criar um DataFrame vazio para armazenar os dados baixados
    dados_acoes = pd.DataFrame()
    # Baixar os dados para cada ação
    for cod in codsa:
        try:
            # Baixar os dados utilizando yfinance e adicionar à DataFrame
            dados_acao = yf.download(cod, start='2024-01-01')['Adj Close'].to_frame()
            dados_acoes = pd.concat([dados_acoes, dados_acao.rename(columns={'Adj Close': cod})], axis=1)
        except Exception as e:
            print(f"Erro ao baixar dados para {codsa}: {e}")

    retornos_diarios = dados_acoes.pct_change().dropna()
    desvio_padrao_diario = retornos_diarios.std()
    desvio_padrao_diario.index = desvio_padrao_diario.index.str.slice(stop = -3)

    # Plotar os desvios padrão diários
    plt.figure()
    plt.bar(desvio_padrao_diario.index, desvio_padrao_diario, color='blue')
    plt.title('Desvio Padrão Diário dos Retornos')
    plt.xlabel('Código da Ação')
    plt.ylabel('Desvio Padrão')
    plt.xticks(rotation='vertical')
    plt.tick_params(axis='x', labelsize=5)
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)