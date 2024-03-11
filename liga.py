import streamlit as st
import pandas as pd

def load_data(file_path):
    """
    Function to load recommended portfolios data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def main():
    # Set page title and description
    st.title('Recommended Portfolios - Liga de Investimentos da UFRN')
    st.write('Welcome to the Investment League of UFRN! Here are the recommended portfolios for your consideration.')

    # Load data
    file_path = 'recommended_portfolios.csv'
    data = load_data(file_path)

    # Display data
    st.write('Recommended Portfolios:')
    st.write(data)

if __name__ == "__main__":
    main()
