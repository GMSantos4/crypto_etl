from extract import fetch_crypto_data
from transform import transform_data
from load import save_to_db

def run_full_etl():
    """
    This function get data from CoinGecho API
    """
    print("STARTING DATA UPDATING...")
    data = fetch_crypto_data()
    cleaned_data = transform_data(data)
    save_to_db(cleaned_data)
    print('DATA UPDATED!')

if __name__ == "__main__":
    run_full_etl()