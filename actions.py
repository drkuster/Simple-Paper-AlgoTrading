import resources as rsrc

def get_account():
    return rsrc.API.get_account()
    

def fetch_price(symbol):
    return rsrc.API.get_last_trade(symbol)

def fetch_position(symbol):
    try:
        return rsrc.API.get_position(symbol)
    except:
        return {}

def place_order(symbol, qty, side, type, time_in_force):
    return rsrc.API.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )
