import resources as rsrc
import pandas as pd

def get_account():
    return rsrc.API.get_account()

def fetch_price(symbol):
    return rsrc.API.get_last_trade(symbol)

def fetch_position(symbol):
    try:
        return rsrc.API.get_position(symbol)
    except:
        return []

def place_order(symbol, qty, side, type, time_in_force):
    return rsrc.API.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )

def fetch_moving_average(ticker):
    NY = 'America/New_York'
    start = pd.Timestamp(str(pd.Timestamp.now().floor('d') - pd.Timedelta(20, unit='d')), tz = NY).isoformat()
    end = pd.Timestamp.now(tz = None).isoformat()
    data = rsrc.API.get_barset([ticker], '15Min', start=start, end=end).df
    
    sum = 0
    count = 0
    
    for index, row in data.iterrows():
        for index, value in row.items():
            if index[1] == 'open':
                sum += value
                count += 1
    
    return sum / count
