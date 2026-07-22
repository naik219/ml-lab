import pandas as pd
import numpy as np

df = pd.read_csv("Test.csv")

Class = "Buys"
Att = ["Age", "Income", "Student", "Credit Rating"]

def entropy(data):
    e = 0
    for c in data[Class].unique():
        p = len(data[data[Class] == c]) / len(data)
        e -= p * np.log2(p)
    return e

def gain(data, att):
    g = entropy(data)
    for v in data[att].unique():
        d = data[data[att] == v]
        g -= (len(d) / len(data)) * entropy(d)
    return g

def id3(data, att):

    if len(data[Class].unique()) == 1:
        return data[Class].iloc[0]

    if len(att) == 0:
        return data[Class].mode()[0]

    best = max(att, key=lambda x: gain(data, x))

    tree = {best: {}}

    newAtt = att.copy()
    newAtt.remove(best)

    for v in data[best].unique():
        tree[best][v] = id3(data[data[best] == v], newAtt)

    return tree

print(id3(df, Att))