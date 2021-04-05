import ccxt
import config



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
    'secret': config.BINANCEUS_SECRET
})
kucoin = ccxt.kucoin({
    'apiKey': config.KUCOIN_KEY,
    'secret': config.KUCOIN_SECRET
})

balance_coinbase = coinbase.fetch_balance()
balance_coinbasepro = coinbasepro.fetch_balance()
balance_binanceus = binanceus.fetch_balance()
balance_kucoin = kucoin.fetch_balance()


