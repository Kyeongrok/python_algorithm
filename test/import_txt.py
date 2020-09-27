import pandas as pd

df = pd.read_csv('report.txt', sep='\t', encoding='utf-8')
print(df)
df.to_excel('report.xlsx')
