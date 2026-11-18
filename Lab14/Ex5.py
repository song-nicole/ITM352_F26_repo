#Get a json file from city of chicago data portal and analyze driver types

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

response_json = response.json()

print("Driver types and license counts")
print(response_json)

response_df = pd.DataFrame.from_records(response_json)
response_df.columns = ["driver_type", "count"]
response_df = response_df.set_index("driver_type") #set rows as driver types
print(response_df)