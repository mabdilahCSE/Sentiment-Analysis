import os
import pandas as pd

data_test = pd.read_csv("tweets.csv")

print(data_test.head())
print(data_test.groupby('movie').count().sort_values(by='tweet', ascending=False))
print(data_test.shape)

