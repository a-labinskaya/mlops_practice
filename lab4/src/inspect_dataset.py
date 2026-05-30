import sys
import pandas as pd

path = sys.argv[1]
df = pd.read_csv(path)

print(df.head())
print(df.shape)
print(df.isna().sum())
