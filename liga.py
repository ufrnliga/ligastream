import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go

# Título da página
st.title('Liga de Investimentos da UFRN')
st.markdown("""Atividade visando formação e capacitação de discentes para desempenho de atividades
            quantitativas no mercado financeiro. A "Liga de Investimentos" é inspirada em modelos de 
            "finance clubs" em universidades de outros países e já amplamente replicados em universidades 
            no Brasil sob a denominação geral de "Liga de Mercado Financeiro". Na liga, discentes são 
            expostos a conteúdos com base na ciência financeira e têm a oportunidade de exercitarem 
            na prática as ferramentas que decorrem do conhecimento científico na área. Essa experiência para 
            os discentes propicia capacitação específica complementar à formação na graduação, conectando 
            especialmente com o "aprender para o fazer". Nesta liga, tratamos apenas do emprego de 
            ferramentas quantitativas como suporte para decisões de investimento no mercado de capitais. """)
st.markdown('---')
# Opções na barra lateral
st.sidebar.header('Onde nos encontrar')
st.sidebar.markdown("[Linkedin](https://www.linkedin.com/company/ufrnliga/)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/ufrnliga/)")
st.sidebar.markdown('---')
st.sidebar.header('Estudos')
opcao_grafico = st.sidebar.radio('', ['Figuras do Ibovespa','Volatilidades no Ibovespa'])
st.sidebar.markdown('---')
st.sidebar.header('Equipe atual')
st.sidebar.markdown("[Gabriel Carvalho, UFPE](https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/)")
st.sidebar.markdown("[Lucas Lima, UFCG](https://www.linkedin.com/in/lucasvitor/)")
st.sidebar.markdown('---')
st.sidebar.header('Orientadores')
st.sidebar.markdown("[Prof. Vinicio Almeida, UFRN](https://www.linkedin.com/in/vinicioalmeida/)")
st.sidebar.markdown("[Prof. Robson Góes, UPE](https://www.linkedin.com/in/robson-g%C3%B3es-de-carvalho-9113b8180/)")

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
    
    assets = [
                "ABEV3.SA", "ALPA4.SA", "ARZZ3.SA", "ASAI3.SA", "AZUL4.SA", "B3SA3.SA", "BBAS3.SA", 
                "BBDC3.SA", "BBDC4.SA", "BBSE3.SA", "BEEF3.SA", "BPAC11.SA", "BRAP4.SA", "BRFS3.SA", "BRKM5.SA", 
                "CASH3.SA", "CCRO3.SA", "CIEL3.SA", "CMIG4.SA", "CMIN3.SA", "COGN3.SA", "CPFE3.SA", "CPLE6.SA", 
                "CRFB3.SA", "CSAN3.SA", "CSNA3.SA", "CVCB3.SA", "CYRE3.SA", "DXCO3.SA", "EGIE3.SA", "ELET3.SA", 
                "ELET6.SA", "EMBR3.SA", "ENEV3.SA", "ENGI11.SA", "EQTL3.SA", "EZTC3.SA", "FLRY3.SA", 
                "GGBR4.SA", "GOAU4.SA", "GOLL4.SA", "HAPV3.SA", "HYPE3.SA", "IGTI11.SA", "IRBR3.SA", "ITSA4.SA", 
                "ITUB4.SA", "JBSS3.SA", "KLBN11.SA", "LREN3.SA", "LWSA3.SA", "MGLU3.SA", "MRFG3.SA", "MRVE3.SA", 
                "MULT3.SA", "NTCO3.SA", "PCAR3.SA", "PETR4.SA", "PETZ3.SA", "PRIO3.SA", "RADL3.SA", 
                "RAIL3.SA", "RAIZ4.SA", "RDOR3.SA", "RENT3.SA", "RRRP3.SA", "SANB11.SA", "SBSP3.SA", "SLCE3.SA", 
                "SMTO3.SA", "SOMA3.SA", "SUZB3.SA", "TAEE11.SA", "TIMS3.SA", "TOTS3.SA", "UGPA3.SA", "USIM5.SA", 
                "VALE3.SA", "VBBR3.SA", "BHIA3.SA", "VIVT3.SA", "WEGE3.SA", "YDUQ3.SA"
            ]

    #download data
    data = yf.download(assets, start='2024-01-01')
    # compute non-compounding, daily returns
    returns = data['Adj Close'].pct_change().dropna()    
    desvio_padrao_diario = returns.std()
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