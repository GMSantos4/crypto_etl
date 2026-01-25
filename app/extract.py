import requests
import time

# this function don't need the API_KEY because it is a public API
def fetch_crypto_data():
    url="https://api.coingecko.com/api/v3/coins/markets"
    params={
        'vs_currency':'usd',
        'order':'market_cap_desc',
        'per_page':25,
        'page':1
    }

    # getting request
    response=requests.get(url,params)

    # returning got response
    for _ in range(5):
        if response.status_code == 200:
            return response.json()
        else:
            time.sleep(5)
    return f'Error {response.status_code} has ocurried.'
    