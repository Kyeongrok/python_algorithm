import pandas as pd

df = pd.read_csv("/Users/mattheu/git/python/demon_user/com/array/hdac_airdrop/trade.csv")
#df['updated_at'] = pd.to_datetime(df['updated_at'], format="%Y/%m/%d")
#df = df.sort_values(by=['updated_at'])
dfTarget = df[['amount', 'buy_user_id', 'updated_at']].copy()
dfTarget = dfTarget[dfTarget.updated_at <= "2018-11-04 05:05:52"]
dfTarget.to_csv('target.csv', index=False)

dfGroup = dfTarget.groupby('buy_user_id').sum()
dfGroup = dfGroup.sort_values(by=['amount'])
