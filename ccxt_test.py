import ccxt, config, json, fetch_funcs


########### Authorization ############
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
#######################################





# balance_coinbase = coinbase.fetch_balance()
# balance_coinbasepro = coinbasepro.fetch_balance()
balance_binanceus = binanceus.fetch_balance()
# balance_kucoin = kucoin.fetch_balance()

# holding_coinbase = coinbase_fetch(balance_coinbase)
# holding_coinbasepro = coinbasepro_fetch(balance_coinbasepro)
holding_binanceus = binanceus_fetch(balance_binanceus)
# holding_kucoin = {}



print(holding_binanceus)


