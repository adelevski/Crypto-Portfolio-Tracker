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


# Get total balance 
def get_total():
    all_holdings = [parse(exchange.fetch_balance()) for exchange in exchanges]
    all_holdings.append(alts.voyager_balance)
    all_holdings.append(alts.metamask_balance)
    total_balance = dsum(all_holdings)
    total_balance['LYXe'] = total_balance.pop('LYXE')
    return dict(sorted(total_balance.items()))


# String Constructor function for CMC API price fetching
def string_maker(balance):
    symbol_string = ''
    for key in balance:
        if key != 'USD':
            symbol_string += key + ','
    return symbol_string[:-1]


def get_prices(total_balance):
    symbol_string = string_maker(total_balance)
    data = cmc.cryptocurrency_quotes_latest(symbol=symbol_string)
    prices = {}
    for key in data.data:
        prices[data.data[key]['symbol']] = data.data[key]['quote']['USD']['price']
    return prices