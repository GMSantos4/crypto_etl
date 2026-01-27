import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text # Importar text para queries seguras

engine = create_engine("sqlite:///data/crypto_db.db")

def get_temporal_serie_data(symbol):
    # Trazer o timestamp ajuda o Streamlit a organizar o eixo X
    query = """
    SELECT timestamp, price 
    FROM crypto_prices 
    WHERE symbol = :symbol 
    ORDER BY timestamp ASC"""
    
    # Usando text() do SQLAlchemy para evitar erros de bind
    df = pd.read_sql(text(query), engine, params={"symbol": symbol})
    
    # Transformar a coluna timestamp em índice para o gráfico de linha
    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')
    return df

def get_cryptocoin_id():
    query = "SELECT DISTINCT symbol FROM crypto_prices"
    df = pd.read_sql(query, engine)
    return df['symbol'].tolist() # Transformar em lista para o selectbox

st.write("Hi there!")
st.write("In this simple application you can see some crypto prices in temporal data series.")

# 1. Pegar lista de moedas
all_coins = get_cryptocoin_id()

with st.container(border=True):
    # 2. Garantir que passamos a lista e pegamos a string selecionada
    coin = st.selectbox("Coins", all_coins)

if coin:
    data = get_temporal_serie_data(coin)

    if not data.empty:
        # 3. Forma correta de usar tabs
        tab1, = st.tabs(["Chart"]) # Note a vírgula para desempacotar a lista
        with tab1:
            st.line_chart(data, height=250)
    else:
        st.warning(f"Sem dados para a moeda {coin}")