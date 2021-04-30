from coinmarketcapapi import CoinMarketCapAPI
import alts, json
from funcs import get_totals, cmc_string_maker, printData
from auth import *
import config
import pandas as pd


cmc = CoinMarketCapAPI(config.CMC_API)

######## Price Fetching ################
totals = get_totals()
symbol_string = cmc_string_maker(totals)
########################################

data = cmc.cryptocurrency_quotes_latest(symbol=symbol_string)

symbols, amounts, quotes, worths = [], [], [], []

for key in data.data:
    symbols.append(data.data[key]['symbol'])
    amounts.append(float(totals[key]))
    quotes.append(float(data.data[key]['quote']['USD']['price']))
    worths.append(float(totals[key])*float(data.data[key]['quote']['USD']['price']))

df = pd.DataFrame(index=symbols)
df['Amount'] = amounts
df['Quote'] = quotes
df['Worth'] = worths
net = df['Worth'].sum()
netWorth = 'Net: $' + f'{net:,.2f}'
df['Amount'] = df['Amount'].map('{:,.4f}'.format)
df['Quote'] = df['Quote'].map('${:,.2f}'.format)
df['Worth'] = df['Worth'].map('${:,.2f}'.format)

print(df)
print(netWorth)

