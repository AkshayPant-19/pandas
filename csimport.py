import pandas as pd
df= pd.read_csv("titanic.csv")  # read a CSV file into a DataFrame
print(df)  # print the first and last 5 rows of the DataFrame
#print(df.to_html())  # convert the DataFrame to an HTML table
#  and print it
json_df = pd.read_json("https://jsonplaceholder.typicode.com/todos/1")  # read JSON data from a URL into a DataFrame
print(json_df)  # print the DataFrame created from JSON data

#selection by columns
