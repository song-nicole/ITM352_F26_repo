# Retrieve and extract the mortgage rate table from the Hawaii Central website.

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

mortgage_table = soup.find("table")
rows = mortgage_table.find_all("tr")

print("Hawaii Mortgage Rates")
current_lender = ""

for row in rows:
    cells = row.find_all(["th", "td"])
    if not cells:
        continue

    if row.find("th"):
        print("\t".join(cell.get_text(" ", strip=True) for cell in cells))
        continue

    lender_cell = cells[0]
    lender_name = lender_cell.find("b")

    if lender_name:
        current_lender = lender_name.get_text(" ", strip=True)
        rate_values = [cell.get_text(" ", strip=True) for cell in cells[1:]]
    else:
        rate_values = [cell.get_text(" ", strip=True) for cell in cells]

    print("\t".join([current_lender, *rate_values]))