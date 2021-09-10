from funcs import get_total
from funcs import get_prices

import pandas as pd



######## Data Fetching ################
total_balance = get_total()
prices = get_prices(total_balance)
########################################





df = pd.DataFrame(index=symbols)
df['Amount'] = amounts
df['Quote'] = quotes
df['Worth'] = worths
net = df['Worth'].sum()
netWorth = 'Net: $' + f'{net:,.2f}'
df['Amount'] = df['Amount'].map('{:,.4f}'.format)
df['Quote'] = df['Quote'].map('${:,.2f}'.format)
df['Worth'] = df['Worth'].map('${:,.2f}'.format)

print(df)
print(netWorth)

