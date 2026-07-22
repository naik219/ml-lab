import pandas as pd

df = pd.read_csv("test.csv")

X = ["Youth", "Low", "Yes", "Fair"]
Class = "Buys"

features = ["Age", "Income", "Student", "Credit Rating"]

best = ""
max_prob = 0

for c in df[Class].unique():

    temp = df[df[Class] == c]

    prob = len(temp) / len(df)

    for i in range(len(features)):
        count = len(temp[temp[features[i]] == X[i]])
        prob *= (count + 1) / (len(temp) + df[features[i]].nunique())

    print(c, "Probability =", prob)

    if prob > max_prob:
        max_prob = prob
        best = c

print("\nPredicted Class =", best)