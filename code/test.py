import pandas as pd

final = pd.read_csv("Final_Dataset.csv")

final["Month"] = pd.to_datetime(final["Month"])

print(final[['Month','Search_Index']].tail(12))