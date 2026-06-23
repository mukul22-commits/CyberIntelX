import pandas as pd

df = pd.read_csv("data/entities.csv")

print("\nTop Organizations\n")

orgs = (
    df[df["type"] == "ORG"]["entity"]
    .value_counts()
    .head(10)
)

print(orgs)

print("\nTop Countries\n")

countries = (
    df[df["type"] == "GPE"]["entity"]
    .value_counts()
    .head(10)
)

print(countries)