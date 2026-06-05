import pandas as pd  # import pandas library with alias pd

data = [100, 23, 45, 67, 89, 90, True, 12.3]  # create a list of values

se = pd.Series(data, index=[1, 2, 3, 4, 5, 6, 7, 8])  # create a Series with custom index labels

print(se.loc[1])  # print the Series value at label 1 using .loc
print(se.iloc[6])  # print the Series value at integer position 6 using .iloc
print(se[se < 3])  # apply boolean indexing to the Series and print values less than 3

titanic = pd.read_csv("titanic.csv")  # read passenger data from a CSV file into a DataFrame
# Ensure Age is numeric before comparing, converting invalid values to NaN
age_values = pd.to_numeric(titanic["Age"], errors="coerce")
age = titanic[age_values > 25]  # filter rows where the Age column is greater than 25
print(age)  # print the filtered DataFrame rows

titanic.shape  # access the shape of the original DataFrame (rows, columns)
age.shape  # access the shape of the filtered DataFrame

multi_data = titanic[["Name", "Age"]]  # select the Name and Age columns from the DataFrame
print(multi_data)  # print the selected columns subset

import pandas as pd  # import pandas library again for the next DataFrame example

df = pd.DataFrame({
    "name": [
        "vinod garkhal",
        "pallavi rathi",
        "brijesh oli",
        "jeewan kumar",
        "sammer verma",
        "meenu verma",
    ],
    "subject": [
        "sst",
        "maths",
        "science",
        "english",
        "ai",
        "hindi",
    ],
    "period no.": [1, 2, 3, 4, 5, 6],
})  # create a DataFrame from a dictionary of lists

df["post"] = ["tgt", "tgt", "tgt", "tgt", "pgt", "tgt"]  # add a new column to the DataFrame
print(df)  # print the complete DataFrame
print("the subject taught are", df["subject"])  # print a label with the subject Series values
print(df["period no."].max())  # print the maximum value from the period no. column
print(df.loc[df["post"] == "pgt"])  # filter rows where post equals 'pgt' using .loc

df.describe  # access the describe attribute for summary statistics without calling it

import pandas as pd  # import pandas library again for the final Series example
day = {"may1": "thu", "may2": "fri", "may3": "sat", "may4": "sun"}
se = pd.Series(day)  # create a Series from a dictionary mapping keys to values
print(se.loc["may3"])  # print the Series value at the label 'may3'
print(se)  # print the entire Series
