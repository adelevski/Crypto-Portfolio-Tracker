# Simple functions for fetching balances from certain exchanges
import alts
from auth import *

# Coinbase
def coinbase_fetch(balance):
    holding = {}
    for data in balance['info']['data']:
        amount = data['balance']['amount']
        currency = data['balance']['currency']
        if float(amount) > 0:
            holding.update({currency: amount})
    return holding

# Coinbase Pro
def coinbasepro_fetch(balance):
    holding = {}
    for asset in balance['info']:
        currency = asset['currency']
        amount = asset['balance']
        if float(amount) > 0:
            holding.update({currency: amount})
    return holding

# Binance US
def binanceus_fetch(balance):
    holding = {}
    for asset in balance['info']['balances']:
        currency = asset['asset']
        amount = asset['free']
        if float(amount) > 0:
            holding.update({currency: amount})
    return holding

# KuCoin
def kucoin_fetch(balance):
    holding = {}
    for asset in balance['info']['data']:
        amount = asset['balance']
        currency = asset['currency']
        if float(amount) > 0:
            holding.update({currency: amount})
    return holding

# Total
def total_fetch(holdings):
    totals = {}
    for holding in holdings:
        for key in holding.keys():
            if key not in totals:
                totals.update({key: holding[key]})
            elif key in totals:
                temp_og = float(totals[key])
                temp_new = float(holding[key])
                totals[key] = str(temp_og + temp_new)
    return totals

# Get totals
def get_totals():
    holding_coinbase = coinbase_fetch(coinbase.fetch_balance())
    holding_coinbasepro = coinbasepro_fetch(coinbasepro.fetch_balance())
    holding_binanceus = binanceus_fetch(binanceus.fetch_balance())
    holding_kucoin = kucoin_fetch(kucoin.fetch_balance())
    holding_voyager = alts.holding_voyager
    holding_metamask = alts.holding_metamask

    all_holdings = [holding_coinbase, holding_coinbasepro, holding_binanceus, holding_kucoin, holding_voyager, holding_metamask]
    totals = total_fetch(all_holdings)

    totals['CELO'] = totals['CGLD']
    totals['LYXe'] = totals['LYXE']
    del totals['CGLD']
    del totals['USD']
    del totals['LYXE']
    return totals
#########################################

# String Constructor function for CMC API price fetching
def cmc_string_maker(totals):
    symbol_string = ''
    for key in totals:
        symbol_string += key + ','
    return symbol_string[:-1]

