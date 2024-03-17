import requests
import json



def sendSPARQLQuery(sparql_query,propriedade):
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

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        cenas = []
        for cena in results["results"]["bindings"]:
            cenas.append(cena[propriedade]["value"])
        return cenas
    else:
        print("Error:", response.status_code)
        print(response.text)
        return []

def getAtores(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?nomeAtor where {{
<{uri}> dbo:starring ?ator.
?ator rdfs:label ?nomeAtor.
FILTER(LANG(?nomeAtor) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"nomeAtor")
    return response

def getRealizadores(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?nomeRealizador where {{
<{uri}> dbp:director ?realizador.
?realizador rdfs:label ?nomeRealizador.
FILTER(LANG(?nomeRealizador) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"nomeRealizador")
    return response



def getProdutores(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?nomeProdutor where {{
<{uri}> dbo:producer ?produtor.
?produtor dbp:name ?nomeProdutor.
FILTER(LANG(?nomeProdutor) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"nomeProdutor")
    return response



def getPaises(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?pais where {{
<{uri}> dbp:country ?pais.
FILTER(LANG(?pais) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"pais")
    return response


def getGenres(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?genre where {{
<{uri}> dbp:Genre  ?genreSemName.
?genreSemName rdfs:label ?genre
FILTER(LANG(?genre) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"genre")
    return response


def getEscritores(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?escritor where {{
<{uri}> dbp:writer  ?escritor.
FILTER(LANG(?escritor) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"escritor")
    return response


def getMusicos(uri):
    sparql_query = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?nomeMusico where {{
<{uri}> dbo:musicComposer ?musico.
?musico dbp:name ?nomeMusico.
FILTER(LANG(?nomeMusico) = 'en').
}} 
"""
    response = sendSPARQLQuery(sparql_query,"nomeMusico")
    return response


# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"


f = open("filmes.json")
filmes = json.load(f)
atores = []
musicos = [] #optional{?s dbo:musicComposer ?music. ?music dbp:name ?musicName. FILTER(LANG(?musicName) = 'en').}
realizadores = [] # optional{?s dbp:director ?director. FILTER (LANG(?director) = 'en').}
produtores = [] #  optional{?s dbo:producer ?producer.?producer dbp:name ?producerName. FILTER (LANG(?producerName) = 'en').}
paises = [] #dbp:country -> ingles
genres = [] #dbp:Genre -> ir bbuscar rdfs:label em ingles
escritores = [] #dbp:writer -> ir buscar ingles
for filme in filmes:
    print(filme["nome"])
    #query para ir buscar atores
    filme["atores"] = getAtores(filme["uri"])
    #query para ir buscar músicos
    filme["musicos"] = getMusicos(filme["uri"])
    #query para ir buscar realizadores
    filme["realizadores"] = getRealizadores(filme["uri"])
    
    #query para ir bbuscar produtores
    filme["produtores"] = getProdutores(filme["uri"])

    #query para ir buscar paises
    filme["paises"] = getPaises(filme["uri"])
    
    #query para ir buscar genres
    filme["genres"] = getGenres(filme["uri"])
    
    #query para ir buscar escritores
    filme["escritores"] = getEscritores(filme["uri"])
    
    
    
    
    
    
    
    
    

   
f = open("filmesMaisInfo.json","w")
json.dump(filmes,f)
f.close()

