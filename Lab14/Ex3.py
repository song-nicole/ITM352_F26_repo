#Scrape names of ITM faculty and grad students

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", itm_url)

itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, "html.parser")
#print(soup.prettify())

#Find all the faculty, which are in h2 tags with class="title"
faculty = soup.find_all("h2", class_="title")

for person in faculty:
    itm_names.append(person.text)
    print("Faculty:", person.text)

print("Total Faculty:", len(faculty))

people_cards = soup.find_all("article", class_="node-faculty")

print("\n\nHTML for the first card:\n")
print(people_cards[0].prettify())

for card in people_cards:
    name = card.find("h2", class_="title").get_text(strip=True)
    email = card.find("div", class_="field-email").get_text(strip=True)
    print(f"{name}: {email}")