#Scrape data from the city of Chicago's data portal
#Print any line with a <title> tag to it

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

print("Retrieving", url)
response = urllib.request.urlopen(url)

for line in response:
    line = line.decode("utf-8").strip()
    if "<title>" in line:
        print(line)