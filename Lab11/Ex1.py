import pandas as pd
import ssl

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

#Temporary fix for link not working due to SSL certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv(csv_file)
print(df.head())

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print("Error reading CSV file:", e)