def transform_data(coarse_data):
    clean_data=[]
    for data in coarse_data:
        clean_data.append({
            'id':data['id'],
            'symbol':data['symbol'].upper(),
            'price':data['current_price'],
            'market_cap':data['market_cap'],
            'timestamp':data['last_updated'],
        })
        return clean_data