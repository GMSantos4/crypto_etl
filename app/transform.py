from datetime import datetime

def transform_data(coarse_data):
    clean_data=[]
    for data in coarse_data:
        clean_data.append({
            'name_id':data['id'],
            'symbol':data['symbol'].upper(),
            'price':data['current_price'],
            'market_cap':data['market_cap'],
            'timestamp':datetime.strptime(data['last_updated'][:10]+' '+data['last_updated'][11:19],"%Y-%m-%d %H:%M:%S"),
        })
    return clean_data