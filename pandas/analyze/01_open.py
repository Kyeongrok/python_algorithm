import pandas as pd
df = pd.read_json("/Users/kyeongrok/Desktop/result.json")

print(df.count())

authors = df['authors']

for author in authors:
    print(len(author))