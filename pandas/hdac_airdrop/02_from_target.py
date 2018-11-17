import pandas as pd

df = pd.read_csv("/Users/mattheu/git/python/demon_user/com/array/hdac_airdrop/target.csv")
df = df.sort_values(by=['updated_at'])
dfTarget = df.groupby(['buy_user_id']).agg({'amount':'sum'})

dfTarget = dfTarget.sort_values(by=['amount'])
dfTarget = dfTarget[dfTarget.amount >= 1000]
dfTarget['e'] = dfTarget['amount'] * 0.01
print(dfTarget)

dfTarget.to_csv('result.csv')
