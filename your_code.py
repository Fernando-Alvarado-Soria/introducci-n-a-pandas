import pandas as pd

df = pd.read_csv("GoogleApps.csv")

print(df.head())
df.info()
print(df.describe())