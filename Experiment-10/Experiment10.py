import pandas as pd

data = {
    "Name": ["Pablo", "Bojack", "Vince", "Marias", None],
    "Age": [32, 20, None, 45, 22],
    "salary": [43440, 54480, 33560, 5543, None],
}

df = pd.DataFrame(data)

df = df.drop_duplicates()
df = df.dropna()
df.columns = df.columns.str.lower()

print("first rows:\n", df.head())
print("\nInfo:\n")
df.info()
print("\nSummary:\n", df.describe())