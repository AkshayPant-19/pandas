import pandas as pd
df= pd.read_csv("titanic.csv", index_col="Name")  # read a CSV file into a DataFrame
print(df)  # print the first and last 5 rows of the DataFrame
#print(df.to_html())  # convert the DataFrame to an HTML table
#  and print it
json_df = pd.read_json("https://jsonplaceholder.typicode.com/todos/1",orient='index')  # read JSON data from a URL into a DataFrame
print(json_df)  # print the DataFrame created from JSON data

#selection by columns
print(df["Survived"])  # print the 'Survived' column of the DataFrame
#print(df[["Name", "Age"]].to_string(index=False))  # print the 'Name' and 'Age' columns of the DataFrame


#selection by rows

#print(df.loc[1])
#print(df.loc["John Smith", ["Age", "Survived"]])

df.iloc[0:4:3]  # print the first row of the DataFrame using integer location-based indexing 