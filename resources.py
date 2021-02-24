import config as cfg
import alpaca_trade_api as tradeapi

API = tradeapi.REST(cfg.API_KEY, cfg.SECRET_KEY, "https://paper-api.alpaca.markets")

# POLYGON = {
#     "POLYGON_URL": "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=2JyZ594I0Pb1CujIGE_8HU72QOl18mjw"    
# }