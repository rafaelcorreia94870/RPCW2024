from bs4 import BeautifulSoup
import requests
import json

def ESTUPIDEZ(name):
    #'DRC', 'U.K.', 'DPRK', 'St. Vincent Grenadines', 'CAR', 'U.S.', 'U.A.E.
    if name == "DRC":
        return "DemocraticRepublicoftheCongo"
    if name == "U.K.":
        return "UnitedKingdom"
    if name == "DPRK":
        return "NorthKorea"
    if name == "St. Vincent Grenadines":
        return "SaintVincentandtheGrenadines"
    if name == "CAR":
        return "CentralAfricanRepublic"
    if name == "U.S.":
        return "UnitedStates"
    if name == "U.A.E.":
        return "UnitedArabEmirates"
    if name == "Côte d'Ivoire":
        return "IvoryCoast"
    return name

def get_flags():
    url = "https://www.worldometers.info/geography/flags-of-the-world/"
    response = requests.get(url)
    #Faz o parse do conteudo da pagina
    soup = BeautifulSoup(response.text, 'html.parser')
    flags = {}
    countries = soup.find_all("div", class_="col-md-4")
    #print(countries)
    for country in countries:
        try:
            name = country.find("div", class_=False).text.strip()
            name = ESTUPIDEZ(name)
            flag = country.a.get("href")
            flag = "https://www.worldometers.info" + flag
            flags[name] = flag
            print(name, flag)
        finally:
            continue
    return flags

def main():
    flags = get_flags()
    data = json.loads(open('datasets/countriesInfo.json', encoding='UTF-8').read())
    set_flags = set(flags.keys())
    for country, flag in flags.items():
        for pais in data:
            nomes = data[pais]["nome"]
            if pais == country or country in nomes:
                data[pais]["flag"] = flag
                set_flags.remove(country)
        
    with open('datasets/countriesInfo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(set_flags)



if __name__ == "__main__":
    main()