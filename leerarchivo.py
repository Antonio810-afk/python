import pandas as pd

df = pd.read_csv("poblacion.csv")
print(df[["Date","COL", "ARG"]])

print(df.head())
print(df.describle())
print(df.tail())
print(df.sample())

print(df.iloc[0])

