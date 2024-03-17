import requests
import json

sparql_endpoint = "http://dbpedia.org/sparql"

sparql_query_template = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select ?s ?nome ?abstract ?duracao ?nomeAtor ?nomeRealizador ?nomeProdutor ?pais ?genre ?nomeEscritor ?nomeMusico where {{
    ?s a dbo:Film.
    
    ?s rdfs:label ?nome.
    FILTER (LANG(?nome) = 'en').

    optional {{
        ?s dbo:abstract ?abstract.
        FILTER (LANG(?abstract) = 'en').
    }}
    
    optional {{
        ?s dbo:runtime ?duracao.
    }}

    optional {{
        ?s dbo:starring ?ator.
        ?ator rdfs:label ?nomeAtor.
        FILTER(LANG(?nomeAtor) = 'en').
    }}

    optional {{
        ?s dbp:director ?realizador.
        ?realizador rdfs:label ?nomeRealizador.
        FILTER(LANG(?nomeRealizador) = 'en').
    }}

    optional {{
        ?s dbo:producer ?produtor.
        ?produtor dbp:name ?nomeProdutor.
        FILTER(LANG(?nomeProdutor) = 'en').
    }}

    optional {{
        ?s dbp:country ?pais.
        FILTER(LANG(?pais) = 'en').
    }}

 

    optional {{
        ?s dbp:genre  ?genreSemName.
        ?genreSemName rdfs:label ?genre
        FILTER(LANG(?genre) = 'en').
    }}
    

    optional {{
        ?s dbo:writer ?escritor.
        ?escritor rdfs:label ?nomeEscritor.
        FILTER(LANG(?nomeEscritor) = 'en').
    }}
   

    optional {{
        ?s dbo:musicComposer ?musico.
        ?musico rdfs:label ?nomeMusico.
        FILTER(LANG(?nomeMusico) = 'en').
    }}
}}
LIMIT {}
OFFSET {}
"""

headers = {
    "Accept": "application/sparql-results+json"
}

results_limit = 10000  # Define o número máximo de resultados por solicitação
offset = 0
all_results = []

while True:
    sparql_query = sparql_query_template.format(results_limit, offset)

    params = {
        "query": sparql_query,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        if not results["results"]["bindings"]:
            break  # Se não houver mais resultados, pare o loop
        all_results.extend(results["results"]["bindings"])
        offset += results_limit
    else:
        print("Error:", response.status_code)
        print(response.text)
        break

# Processar todos os resultados como antes
#?nome ?abstract ?duracao ?nomeAtor ?nomeRealizador ?nomeProdutor ?pais ?genre ?nomeEscritor ?nomeMusico
films_data = {}
for result in all_results:
    uri = result["s"]["value"]
    nome = result["nome"]["value"]
    nomeAtor = result.get("nomeAtor", {}).get("value", None)
    nomeRealizador = result.get("nomeRealizador", {}).get("value", None)
    nomeEscritor = result.get("nomeEscritor", {}).get("value", None)
    nomeMusico = result.get("nomeMusico", {}).get("value", None)

    descricao = result.get("abstract", {}).get("value", None)
    duracao = result.get("duracao", {}).get("value", None)
    nomeProdutor = result.get("nomeProdutor", {}).get("value", None)
    pais = result.get("pais", {}).get("value", None)
    genero = result.get("genre", {}).get("value", None)


    if uri in films_data:
        if nomeAtor and nomeAtor not in films_data[uri]["atores"]:
            films_data[uri]["atores"].append(nomeAtor)
        if nomeRealizador and nomeRealizador not in films_data[uri]["realizadores"]:
            films_data[uri]["realizadores"].append(nomeRealizador)
        if nomeEscritor and nomeEscritor not in films_data[uri]["escritores"]:
            films_data[uri]["escritores"].append(nomeEscritor)
        if nomeMusico and nomeMusico not in films_data[uri]["musicos"]:
            films_data[uri]["musicos"].append(nomeMusico)
        if descricao and descricao not in films_data[uri]["descricao"]:
            films_data[uri]["descricao"].append(descricao)
        if duracao and duracao not in films_data[uri]["duracao"]:
            films_data[uri]["duracao"].append(duracao)
        if nomeProdutor and nomeProdutor not in films_data[uri]["produtores"]:
            films_data[uri]["produtores"].append(nomeProdutor)
        if pais and pais not in films_data[uri]["pais"]:
            films_data[uri]["pais"].append(pais)
        if genero and genero not in films_data[uri]["genero"]:
            films_data[uri]["genero"].append(genero)
    else:
        films_data[uri] = {
            "filme": nome,
            "atores": {nomeAtor} if nomeAtor else [],
            "realizadores": {nomeRealizador} if nomeRealizador else [],
            "escritores":  {nomeEscritor} if nomeEscritor else [],
            "musicos":  {nomeMusico} if nomeMusico else [],
            "descricao": {descricao} if descricao else [],
            "duracao": {duracao} if duracao else [],
            "produtores": {nomeProdutor} if nomeProdutor else [],
            "pais": {pais} if pais else [],
            "genero": {genero} if genero else []
        }

films_list = list(films_data.values())

with open("cinema2.json", "w") as f:
    json.dump(films_list, f)