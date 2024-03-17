import requests
import json

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select ?s ?nome ?abstract ?duracao where {
    ?s a dbo:Film.
     optional {?s dbo:abstract ?abstract.
              FILTER (LANG(?abstract) = 'en').
}
     ?s rdfs:label ?nome.
      optional {?s dbo:runtime ?duracao.}
    
      FILTER (LANG(?nome) = 'en').
   
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
response = requests.get(sparql_endpoint, params=params, headers=headers,timeout=1000)
print("Headers sent in the request:")
print(response.request.headers)

print("\nParameters sent in the request:")
print(response.request.url)  # This will show the full URL with parameters

filmes = []
# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    # Print the results
    for result in results["results"]["bindings"]:
        filme = {"uri":result["s"]["value"]}
        filme["nome"] = result["nome"]["value"]
        if "abstract" in result: filme["abstract"] = result["abstract"]["value"]
        if "duracao" in result: filme["duracao"] = float(result["duracao"]["value"])/60
        filmes.append(filme)
    f = open("filmes.json","w")
    json.dump(filmes,f)
    f.close()
else:
    print("Error:", response.status_code)
    print(response.text)

