#get public license data from city of chicago data portal

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)
json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)

results_df = pd.DataFrame.from_records(results)
results_df.info()


vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public vehicles and fuel sources")
vehicles.info()

vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)

#"Requests made without an app_token will be subject to strict throttling limits."
#Above message means that you will be limited to a certain number of requests per day
