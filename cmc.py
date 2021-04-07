from coinmarketcapapi import CoinMarketCapAPI
import alts, json
from fetch_funcs import get_totals, cmc_string_maker
from auth import *
import config


cmc = CoinMarketCapAPI(config.CMC_API)

######## Price Fetching ################
totals = get_totals()
symbol_string = cmc_string_maker(totals)
########################################

total_holdings = 0.0
data = cmc.cryptocurrency_quotes_latest(symbol=symbol_string)
for key in data.data:
    symbol = data.data[key]['symbol'] 
    price = data.data[key]['quote']['USD']['price']
    print(f"The price of {symbol} is {price} and you currently hold {totals[key]}")
    total_holdings += float(price) * float(totals[key])
print(f"For a total of ${total_holdings}")
