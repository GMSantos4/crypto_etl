import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/crypto_db.db")

def get_temporal_serie_data(symbol):
    query = """
    SELECT timestamp, price 
    FROM crypto_prices 
    WHERE symbol = :symbol 
    ORDER BY timestamp ASC"""

    df = pd.read_sql(text(query), engine, params={"symbol": symbol})

    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')
    return df

def get_cryptocoin_id():
    query = "SELECT DISTINCT symbol FROM crypto_prices"
    df = pd.read_sql(query, engine)
    return df['symbol'].tolist()

st.write("Hi there!")
st.write("In this simple application you can see some crypto prices in temporal data series.")

all_coins = get_cryptocoin_id()

with st.container(border=True):
    coin = st.selectbox("Coins", all_coins)

if coin:
    data = get_temporal_serie_data(coin)

    if not data.empty:
        tab1, = st.tabs(["Chart"])
        with tab1:
            st.line_chart(data, height=250)
    else:
        st.warning(f"No data for {coin}")