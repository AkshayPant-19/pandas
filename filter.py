import pandas as pd
df= pd.read_csv("pokemon.csv", index_col="Name")

#filtering the DataFrame to include only rows where the "Type 1" column is equal to "Fire"
grass=df[(df["Type 1"] == "Grass") &
        (df["Type 2"] == "Flying")]
print(grass)
legendary=df[df["Legendary"] == 1]
#print(legendary)