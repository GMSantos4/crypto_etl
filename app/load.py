from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import sessionmaker

import datetime
import os

Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = 'crypto_prices'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name_id = Column(String)
    symbol = Column(String)
    price = Column(Float)
    market_cap = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.now())

def save_to_db(data_list):
    # Verifying if the directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    engine = create_engine('sqlite:///data/crypto_db.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in data_list:
        obj = CryptoPrice(
            name_id = item['name_id'],
            symbol = item['symbol'],
            price = item['price'],
            market_cap = item['market_cap'],
            timestamp = item['timestamp'],
        )
        session.merge(obj)

    session.commit()
    session.close()