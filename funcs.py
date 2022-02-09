import alts
from auth import exchanges
from auth import cmc
import pandas as pd
from collections import defaultdict


# Retrieve relevant information from ccxt response
def parse(response):
    return {k:v for k,v in response['total'].items() if v}


# Aggregate all dictionaries
def dsum(dicts):
    ret = defaultdict(float)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)


# Get total balance and balance per exchange
def get_total():
    all_holdings = {}
    for name, exchange in exchanges.items():
        all_holdings[name] = parse(exchange.fetch_balance())
    all_holdings['Voyager'] = alts.voyager_balance
    all_holdings['MetaMask'] = alts.metamask_balance
    total_balance = dsum(list(all_holdings.values()))
    total_balance['LYXe'] = total_balance.pop('LYXE')
    return dict(sorted(total_balance.items())), all_holdings


# String Constructor function for CMC API price fetching
def string_maker(balance):
    symbol_string = ''
    for key in balance:
        if key != 'USD':
            symbol_string += key + ','
    return symbol_string[:-1]


# Getting prices from Coin Market Cap
def get_prices(balance):
    symbol_string = string_maker(balance)
    data = cmc.cryptocurrency_quotes_latest(symbol=symbol_string)
    prices = {}
    for key in data.data:
        prices[data.data[key]['symbol']] = data.data[key]['quote']['USD']['price']
    return prices


# Formatting data in to dataframes, formatting (if form = True) and returning it along with total value
def get_df(balance, prices, form=False):
    if 'LYXE' in balance.keys():
        balance['LYXe'] = balance.pop('LYXE')
    df = pd.DataFrame.from_dict(balance, columns=['amount'], orient='index')
    df['price'] = df.index.map(prices)
    df.fillna(1.0, inplace=True)
    df['value'] = df['price'] * df['amount']
    total_value = df['value'].sum()
    df['weight'] = (df['value'] / total_value) * 100
    if form:
        df['amount'] = df['amount'].map('{:,.4f}'.format)
        df['price'] = df['price'].map('${:,.2f}'.format)
        df['value'] = df['value'].map('${:,.2f}'.format)
        df['weight'] = df['weight'].map('{:,.2f}%'.format)
    return df, total_value