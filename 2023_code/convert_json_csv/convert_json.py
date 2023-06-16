import pandas as pd

json_data = pd.read_json("result.json")
print(type(json_data))

print(json_data.shape)
print(json_data.columns)
print(json_data.head(5))
json_data.to_csv("csv_result.csv")