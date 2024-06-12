from bs4 import BeautifulSoup
import requests
import json



url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"
response = requests.get(url)
#Faz o parse do conteudo da pagina
soup = BeautifulSoup(response.text, 'html.parser')


data = json.loads(open('datasets/countriesInfo.json', encoding='UTF-8').read())

countriesTemperature = {}
continents = ["Africa","","Asia","Europa","America do Norte","America do Sul","Oceania"]
for table in soup.find_all("table",class_="wikitable"):
    continent = continents.pop(0)
    if continent == "":
        continue
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        countryName = cells[2].text.strip().replace(" ","").split("[")[0].replace("*","")
        if countryName=="DemocraticCongo":
            countryName = "DemocraticRepublicoftheCongo"
        if countryName=="Congo":
            countryName = "RepublicoftheCongo"
        if countryName=="Gambia":
            countryName = "TheGambia"
        if countryName=="Côted'Ivoire":
            countryName = "IvoryCoast"
        if countryName=="Taiwan":
            continue
        if countryName=="Timor-Leste":
            countryName = "EastTimor"
        if countryName=="Czechia":
            countryName = "CzechRepublic"
        if countryName=="Kosovo":
            continue
        if countryName=="VaticanCity":
            countryName="HolySee"
        if countryName=="CookIslands":
            continue
        if countryName=="FederatedStatesofMicronesia":
            countryName="Micronesia"
        if countryName=="Niue":
            continue
        if countryName in data:
            data[countryName]["continente"] = continent
data["Palestine"]["continente"] = "Asia"
            
        
with open('datasets/countriesInfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



