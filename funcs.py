# Simple functions for fetching balances from certain exchanges
import alts
from auth import *
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

# Get total
def get_total():
    all_holdings = [
        parse(coinbase.fetch_balance()),
        parse(coinbasepro.fetch_balance()),
        parse(binanceus.fetch_balance()),
        parse(kucoin.fetch_balance()),
        alts.voyager_balance,
        alts.metamask_balance]

    total = dsum(all_holdings)

    totals['LYXe'] = totals['LYXE']
    del totals['LYXE']

    return dict(sorted(total.items()))

# String Constructor function for CMC API price fetching
def string_maker(totals):
    symbol_string = ''
    for key in totals:
        if key != 'USD':
            symbol_string += key + ','
    return symbol_string[:-1]
