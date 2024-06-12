from bs4 import BeautifulSoup
import requests
import json



url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature"
response = requests.get(url)
#Faz o parse do conteudo da pagina
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table")
body = table.tbody

data = json.loads(open('datasets/dbpediaCountries.json', encoding='UTF-8').read())

countriesTemperature = {}
for row in body.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) > 2:
        country = cells[1].text
        temperature = cells[2].text
        temperature = temperature.split("\xa0")[0]
        country = country.replace(" ","").strip()
        if country=="Bahamas":
            country = "TheBahamas"
        if country=="Gambia":
            country = "TheGambia"
        if country=="VaticanCity":
            country = "HolySee"
        if country=="FederatedStatesofMicronesia":
            country = "Micronesia"
        if country=="Timor-Leste":
            country = "EastTimor"
        countriesTemperature[country] = temperature

for country in data:
    if country in countriesTemperature:
        data[country]["temperatura media"] = countriesTemperature[country]
        

f = open("datasets/final_countries2.json","w", encoding='UTF-8')
json.dump(data,f,indent=4)


