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
    amount = float(totals[key]) 
    quote = float(data.data[key]['quote']['USD']['price'])
    worth = amount*quote
    print(f"{symbol}: {amount:.2f} at ${quote:.2f} worth ${worth:.2f}")
    total_holdings += worth
print(f"Total: ${total_holdings:.2f}")
