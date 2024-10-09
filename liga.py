import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Liga UFRN')

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
opcao_grafico = st.sidebar.radio('', ['Figuras do Ibovespa', 'CDI x Ibovespa'])
st.sidebar.markdown('---')
st.sidebar.header('Equipe atual')
st.sidebar.markdown("[Gabriel Carvalho, UFPE](https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/)")
st.sidebar.markdown("[Georgio Kokkosis, UFPE](https://www.linkedin.com/in/georgio-kokkosis-4450a579/)")
st.sidebar.markdown("[Lucas Lima, UFCG](https://www.linkedin.com/in/lucasvitor/)")
st.sidebar.markdown("[Luiz Gonçalves, UFPE](https://www.linkedin.com/in/luiz-f-gon%C3%A7alves-da-silva-763561244/)")
st.sidebar.markdown("[Paulo Lima, UFRN](https://www.linkedin.com/in/paulorog/)")
st.sidebar.header('Orientadores')
st.sidebar.markdown("[Prof. Vinicio Almeida, UFRN](https://www.linkedin.com/in/vinicioalmeida/)")
st.sidebar.markdown("[Prof. Robson Góes, UPE](https://www.linkedin.com/in/robson-g%C3%B3es-de-carvalho-9113b8180/)")
st.sidebar.markdown('---')
st.sidebar.markdown("[Linkedin](https://www.linkedin.com/company/ufrnliga/)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/ufrnliga/)")

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


if opcao_grafico == 'CDI x Ibovespa':
    st.subheader('CDI x Ibovespa')
    st.markdown("""Atualizado diariamente.""")
    st.markdown('---')
    
    def extracao_bcb(codigo, data_inicio, data_fim):
        url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codigo, data_inicio, data_fim)
        df = pd.read_json(url)
        df.set_index('data', inplace=True)
        df.index = pd.to_datetime(df.index, dayfirst=True)
        df.columns = ['SELIC']
        df['SELIC'] = df['SELIC']/100
        return df

    data_inicio = '01/05/1993' 
    data_fim = '30/04/2024'
    dados=[]
    dados = extracao_bcb(4390, data_inicio=data_inicio, data_fim=data_fim)
    indices = ['^BVSP']

    for i in indices:
        dados[i] = yf.download(i, start='1993-05-01', end='2024-04-30', interval='1mo')['Adj Close'].pct_change()

    dados = dados.iloc[1:]
    dados = dados + 1

    acumulado = dados.cumprod()

    # Plot
    plt.figure()
    plt.plot(acumulado)
    plt.xlabel('Anos')
    plt.ylabel('Retornos acumulados')
    plt.title('CDI x Ibovespa')
    plt.legend(['CDI', 'Ibovespa'])  # Adiciona legendas    
    st.pyplot(plt)
