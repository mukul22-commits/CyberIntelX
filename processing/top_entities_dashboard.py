import pandas as pd

df = pd.read_csv("data/entities.csv")

orgs = (
    df[df["type"] == "ORG"]["entity"]
    .value_counts()
    .head(10)
)

countries = (
    df[df["type"] == "GPE"]["entity"]
    .value_counts()
    .head(10)
)

orgs.to_csv("data/top_orgs.csv")
countries.to_csv("data/top_countries.csv")

print("Entity summaries generated")