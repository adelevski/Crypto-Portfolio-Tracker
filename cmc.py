from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, alts
from pprint import pprint
from fetch_funcs import *
from auth import *


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


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'3',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '4d28581b-33ae-428c-85a4-a2797ba109b4',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for i in range(3):
    print(data.get('data')[i]['name'])
    print(data.get('data')[i]['quote']['USD']['price'])

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)