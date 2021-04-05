import ccxt
import config
import json


# Coinbase
def coinbase_fetch(balance):
    holding = {}
    for data in balance['info']['data']:
        amount = data['balance']['amount']
        currency = data['balance']['currency']
        if float(amount) > 0:
            holding.update({currency: amount})
    return holding


coinbase = ccxt.coinbase({
    'apiKey': config.COINBASE_KEY,
    'secret': config.COINBASE_SECRET
})
coinbasepro = ccxt.coinbasepro({
    'apiKey': config.COINBASE_PRO_KEY,
    'secret': config.COINBASE_PRO_SECRET,
    'password': config.COINBASE_PRO_PASSPHRASE
})
binanceus = ccxt.binanceus({
    'apiKey': config.BINANCEUS_KEY,
    'secret': config.BINANCEUS_SECRET,
    'nonce': ccxt.Exchange.milliseconds
})
kucoin = ccxt.kucoin({
    'apiKey': config.KUCOIN_KEY,
    'secret': config.KUCOIN_SECRET,
    'password': config.KUCOIN_PASSWORD
})

balance_coinbase = coinbase.fetch_balance()
balance_coinbasepro = coinbasepro.fetch_balance()
balance_binanceus = binanceus.fetch_balance()
balance_kucoin = kucoin.fetch_balance()

holding_coinbase = coinbase_fetch(balance_coinbase)
holding_coinbasepro = {}
holding_binanceus = {}
holding_kucoin = {}

print(holding_coinbase)





