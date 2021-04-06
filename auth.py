import ccxt, config


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