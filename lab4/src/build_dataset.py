import argparse
import pandas as pd
from catboost.datasets import titanic

parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True, choices=["selected", "age_filled", "sex_encoded"])
parser.add_argument("--output", default="lab4/data/titanic.csv")
args = parser.parse_args()

train_df, _ = titanic()
df = train_df[["Pclass", "Sex", "Age"]].copy()

if args.version in ["age_filled", "sex_encoded"]:
    df["Age"] = df["Age"].fillna(df["Age"].mean())

if args.version == "sex_encoded":
    df = pd.get_dummies(df, columns=["Sex"])

df.to_csv(args.output, index=False)
print(df.head())
print(df.info())
