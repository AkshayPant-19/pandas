import pandas as pd
df= pd.read_csv("titanic.csv", index_col="Name") 

passenger_name=input("Enter passenger name: ")  # read a CSV file into a DataFrame
try:
    print(df.loc[passenger_name])  # print the first and last 5 rows of the DataFrame
except Exception as e:
    print(f"Error: {e}")