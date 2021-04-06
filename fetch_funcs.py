# Simple functions for fetching balances from certain exchanges

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