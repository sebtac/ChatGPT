

import pandas as pd
import numpy as np

# Load USO data from Yahoo
uso = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/USO?period1=946665600&period2=1598188800&interval=1d&events=history')

# Calculate Moving Average
uso['MA50'] = uso['Close'].rolling(window=50).mean()
uso['MA200'] = uso['Close'].rolling(window=200).mean()

# Calculate Moving Average Crossover
uso['MA50-MA200'] = uso['MA50'] - uso['MA200']

# Calculate the Direction of the Moving Average Crossover
uso['MA50-MA200 Direction'] = np.where(uso['MA50-MA200'] > 0, 1, 0)
uso['MA50-MA200 Direction'] = np.where(uso['MA50-MA200'] < 0, -1, uso['MA50-MA200 Direction'])

# Print the DataFrame
print(uso)