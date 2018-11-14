import pandas as pd

dfBuy = pd.read_csv("./buy.csv")
dfSell = pd.read_csv("./sell.csv")

dfTotal = pd.concat([dfBuy, dfSell])

dfBuy.groupby(['user_id']).sum()
print(dfTotal['amount'])


