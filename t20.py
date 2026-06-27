import pandas as pd
df= pd.read_csv('t20.csv')
print(df.head())
print(df[df['potm'] == 'Lungi Ngidi'])