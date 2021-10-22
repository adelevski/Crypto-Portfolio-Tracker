from funcs import get_total
from funcs import get_prices
import pandas as pd


# data fetching
total_balance = get_total()
prices = get_prices(total_balance)


# dataframe creation and processing
df = pd.DataFrame.from_dict(total_balance, columns=['amount'], orient='index')
df['price'] = df.index.map(prices)
df.fillna(1.0, inplace=True)
df['value'] = df['price'] * df['amount']
total_value = df['value'].sum()
df['weight'] = (df['value'] / total_value) * 100


# dataframe formatting for presentation
df['amount'] = df['amount'].map('{:,.4f}'.format)
df['price'] = df['price'].map('${:,.2f}'.format)
df['value'] = df['value'].map('${:,.2f}'.format)
df['weight'] = df['weight'].map('{:,.2f}%'.format)


print(df)
print(f"Total value: ${total_value:.2f}")
