import streamlit as st

def main():
    # Set page title and description
    st.title('Recommended Portfolios - Liga de Investimentos da UFRN')
    st.write('Welcome to the Investment League of UFRN! Here are the recommended portfolios for your consideration.')

    # Display sample recommended portfolios
    portfolios = {
        'Portfolio 1': {'Stocks': 'AAPL, GOOGL, MSFT', 'Bonds': 'AGG, BND, TLT'},
        'Portfolio 2': {'Stocks': 'AMZN, FB, NFLX', 'Bonds': 'BNDX, LQD, MUB'},
        'Portfolio 3': {'Stocks': 'JNJ, V, PG', 'Bonds': 'BND, TLT, VCIT'}
    }

    st.write('Recommended Portfolios:')
    for name, assets in portfolios.items():
        st.write(f'Portfolio: {name}')
        st.write(f'- Stocks: {assets["Stocks"]}')
        st.write(f'- Bonds: {assets["Bonds"]}')
        st.write('---')

if __name__ == "__main__":
    main()