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
        if nomeAtor :
            films_data[uri]["atores"].add(nomeAtor)
        if nomeRealizador :
            films_data[uri]["realizadores"].add(nomeRealizador)
        if nomeEscritor :
            films_data[uri]["escritores"].add(nomeEscritor)
        if nomeMusico:
            films_data[uri]["musicos"].add(nomeMusico)
        if descricao:
            films_data[uri]["descricao"].add(descricao)
        if duracao:
            films_data[uri]["duracao"].add(duracao)
        if nomeProdutor:
            films_data[uri]["produtores"].add(nomeProdutor)
        if pais:
            films_data[uri]["pais"].add(pais)
        if genero:
            films_data[uri]["genero"].add(genero)
    else:
        films_data[uri] = {
            "filme": nome,
            "atores": {nomeAtor} if nomeAtor else set(),
            "realizadores": {nomeRealizador} if nomeRealizador else set(),
            "escritores":  {nomeEscritor} if nomeEscritor else set(),
            "musicos":  {nomeMusico} if nomeMusico else set(),
            "descricao": {descricao} if descricao else set(),
            "duracao": {duracao} if duracao else set(),
            "produtores": {nomeProdutor} if nomeProdutor else set(),
            "pais": {pais} if pais else set(),
            "genero": {genero} if genero else set()
        }

films_list = list(films_data.values())

with open("cinema2.json", "w") as f:
    json.dump(films_list, f)
    # Convert the sets to lists before serializing
    for film_data in films_list:
        film_data["atores"] = list(film_data["atores"])
        film_data["realizadores"] = list(film_data["realizadores"])
        film_data["escritores"] = list(film_data["escritores"])
        film_data["musicos"] = list(film_data["musicos"])
        film_data["descricao"] = list(film_data["descricao"])
        film_data["duracao"] = list(film_data["duracao"])
        film_data["produtores"] = list(film_data["produtores"])
        film_data["pais"] = list(film_data["pais"])
        film_data["genero"] = list(film_data["genero"])

    # Write the serialized data to the file
    with open("cinema2.json", "w") as f:
        json.dump(films_list, f)