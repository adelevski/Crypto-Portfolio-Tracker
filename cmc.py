from coinmarketcapapi import CoinMarketCapAPI
import alts, json
from funcs import get_totals, cmc_string_maker, printData
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
    printData(symbol, amount, quote, worth)
    total_holdings += worth
print(f"Total: ${total_holdings:.2f}")
