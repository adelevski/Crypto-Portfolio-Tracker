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