from coinmarketcapapi import CoinMarketCapAPI
import alts
from fetch_funcs import *
from auth import *


cmc = CoinMarketCapAPI('4d28581b-33ae-428c-85a4-a2797ba109b4')


######### Balance Fetching ##############
holding_coinbase = coinbase_fetch(coinbase.fetch_balance())
holding_coinbasepro = coinbasepro_fetch(coinbasepro.fetch_balance())
holding_binanceus = binanceus_fetch(binanceus.fetch_balance())
holding_kucoin = kucoin_fetch(kucoin.fetch_balance())
holding_voyager = alts.holding_voyager
holding_metamask = alts.holding_metamask

all_holdings = [holding_coinbase, holding_coinbasepro, holding_binanceus, holding_kucoin, holding_voyager, holding_metamask]
totals = total_fetch(all_holdings)
#########################################


######## Price Fetching ################
symbol_string = cmc_string_maker(totals)
########################################


# data = cmc.cryptocurrency_quotes_latest(symbol='BTC,ETH')
# print(data)