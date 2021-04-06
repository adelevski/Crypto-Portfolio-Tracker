import ccxt, config, json
from fetch_funcs import *


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


######### Balance Fetching ##############
holding_coinbase = coinbase_fetch(coinbase.fetch_balance())
holding_coinbasepro = coinbasepro_fetch(coinbasepro.fetch_balance())
holding_binanceus = binanceus_fetch(binanceus.fetch_balance())
holding_kucoin = kucoin_fetch(kucoin.fetch_balance())

all_holdings = [holding_coinbase, holding_coinbasepro, holding_binanceus, holding_kucoin]
totals = total_fetch(all_holdings)
#########################################



# print(holding_coinbase)
# print(holding_coinbasepro)
# print(holding_binanceus)
# print(holding_kucoin)

print(totals)