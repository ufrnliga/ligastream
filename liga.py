import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define a cor de fundo e texto padrão
cor_fundo = '#000000'  # Preto
cor_texto = '#FFFF00'  # Amarelo

# Configurações de estilo para o Streamlit
st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 1000px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }}
        img {{
            max-width: 50%;
        }}
        .reportview-container .main {{
            color: {cor_texto};
            background-color: {cor_fundo};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Título da página
st.title('Liga de Investimentos da UFRN')

# Carregar e exibir o logo da liga
logo_url = '/home/vinicio/repo/ligastream/liga.jpg'
st.sidebar.image(logo_url, caption='Logo da Liga de Investimentos da UFRN')

# Opção para plotar um gráfico (coloque o código    do gráfico aqui)
st.sidebar.header('Opções')
opcao_grafico = st.sidebar.selectbox('Selecione uma opção', ['Gráfico'])

if opcao_grafico == 'Gráfico':
    # Código para plotar um gráfico (exemplo)
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de exemplo')
    st.pyplot(plt)
