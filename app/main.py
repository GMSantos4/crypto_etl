from extract import fetch_crypto_data
from transform import transform_data
from load import save_to_db

def main():
    data = fetch_crypto_data()
    cleaned_data = transform_data(data)
    save_to_db(cleaned_data)

if __name__ == "__main__":
    main()