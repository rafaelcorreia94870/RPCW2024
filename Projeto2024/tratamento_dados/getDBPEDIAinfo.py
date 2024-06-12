import requests
import json

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
select distinct ?pais (SAMPLE(?capital) AS ?cap) ?conduz ?moeda (SAMPLE(?latitude) AS ?lat) (SAMPLE(?longitude) AS ?long) where {
?country a dbo:Country;
rdfs:label ?pais.
{
?country dbo:capital ?capitalURI.
?capitalURI rdfs:label ?capital.
filter(lang(?capital)="en").
}
UNION
{
?country dbp:capital ?capitalURI.
?capitalURI rdfs:label ?capital.
filter(lang(?capital)="en").
}
UNION
{
?country dbp:capital ?capital.
filter(lang(?capital)="en").
}


?country geo:lat ?latitude.
?country geo:long ?longitude.

optional{ ?country dbp:drivesOn ?conduz.}
optional{
?country dbo:currency ?moedaURI.
?moedaURI rdfs:label ?moeda.
filter(lang(?moeda)="en").
}

filter(lang(?pais)="en").

} 


"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": sparql_query,
    "format": "json"
}

# Send the SPARQL query using requests
response = requests.get(sparql_endpoint, params=params, headers=headers)

paises = {}
# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    # Print the results
    for result in results["results"]["bindings"]:
        pais = {}
        if "lat" in result:
            pais["latitude"] = result["lat"]["value"]
        if "long" in result:
            pais["longitude"] = result["long"]["value"]
        if "cap" in result:
            pais["capital"] = result["cap"]["value"]
        if "conduz" in result:
            pais["conduz"] = result["conduz"]["value"]
        if "moeda" in result:
            pais["moeda"] = result["moeda"]["value"]
        paisNome = result["pais"]["value"].replace(" ","")
        if paisNome not in paises:
            paises[paisNome] = pais
    data_original = json.loads(open('datasets/final_countries.json', encoding='UTF-8').read())
    for pais,data in data_original.items():
        if pais in paises:
            if "conduz" in paises[pais]:
                data_original[pais]["lado em que conduz"] = paises[pais]["conduz"]
            if "moeda" in paises[pais]:
                data_original[pais]["moeda"] = paises[pais]["moeda"]
            if data["latitude"] == "":
                data_original[pais]["latitude"] = paises[pais]["latitude"]
                data_original[pais]["longitude"] = paises[pais]["longitude"]
            if data["capital"] == "":
                if pais=="Singapore":
                    data_original[pais]["capital"] = "Singapore"
                else:
                    data_original[pais]["capital"] = paises[pais]["capital"]
                
            
    f = open("datasets/dbpediaCountries.json","w", encoding='UTF-8')
    json.dump(data_original,f)
    f.close()
else:
    print("Error:", response.status_code)
    print(response.text)

