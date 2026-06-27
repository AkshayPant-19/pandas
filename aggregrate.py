import pandas as pd
df= pd.read_csv('pokemon.csv')
print(df.mean(numeric_only=True))
#all function
#.sum() - returns the sum of the values for the requested axis
#.min() - returns the minimum value for the requested axis
#.max() - returns the maximum value for the requested axis
#.std() - returns the standard deviation for the requested axis
#.count() - returns the number of non-null values for the requested axis
