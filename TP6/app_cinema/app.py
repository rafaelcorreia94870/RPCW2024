from flask import Flask, render_template, url_for
from datetime import datetime
import requests
 
app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime("%Y-%m-%dT%H:%M:%S")


#trasformar os dados do sparql num dicionario em que são guardados os atores,realizadores..., numa lista
def tratardados(dados):
    filme = {"title": None, "duration": "-", 
            "description": "-", "directors": set(),"actors": set(),"genres": set(),"country": set(),"composers": set(),"producers": set(),"screenwriters": set(),}
    for line in dados:
        if "title" in line and not filme["title"]:
            filme["title"] = line["title"]["value"]
        if "duration" in line and filme["duration"] == "-":
            filme["duration"] = line["duration"]["value"]
        if "description" in line and filme["description"] == "-":
            filme["description"] = line["description"]["value"]
        if "director" in line:
            filme["directors"].add(line["director"]["value"].split("/")[-1])
        if "actor" in line:
            filme["actors"].add(line["actor"]["value"].split("/")[-1])
        if "genre" in line:
            filme["genres"].add(line["genre"]["value"].split("/")[-1])
        if "country" in line:
            filme["country"].add(line["country"]["value"].split("/")[-1])
        if "composer" in line:
            filme["composers"].add(line["composer"]["value"].split("/")[-1])
        if "producer" in line:
            filme["producers"].add(line["producer"]["value"].split("/")[-1])
        if "screenwriter" in line:
            filme["screenwriters"].add(line["screenwriter"]["value"].split("/")[-1])
    return filme
    
#GraphDB endpoint
graphdb_endpoint = "http://epl.di.uminho.pt:7200/repositories/cinema2024"

@app.route("/")
def index():
    return render_template('index.html',data = {"data":data_iso_formatada})

@app.route("/filmes")
def filmes():
    sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
select ?s ?title ?duration  where {
    ?s a :Film;
    :title ?title;
    optional { ?s :duration ?duration.}
}
    """
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        return render_template("filmes.html", data = dados)
    else:
        return render_template("empty.html",data = {"data":data_iso_formatada})


@app.route("/realizadores")
def realizadores():
    sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
select ?director (COUNT(?s) as ?nfilmes) where {
    ?s a :Film .
    ?s :hasDirector ?director.
} 
GROUP BY (?director)
ORDER BY DESC (?nfilmes)
    """
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        return render_template("realizadores.html", data = dados)
    else:
        return render_template("empty.html",data = {"data":data_iso_formatada})
    

@app.route("/atores")
def atores():
    sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
select ?actor (COUNT(?s) as ?nfilmes) where {
    ?s a :Film .
    ?s :hasActor ?actor.
} 
GROUP BY (?actor)
ORDER BY DESC (?nfilmes)
    """
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        return render_template("atores.html", data = dados)
    else:
        return render_template("empty.html",data = {"data":data_iso_formatada})





@app.route("/filmes/<string:name>")
def filme(name):
    sparql_query = f"""
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
select * where {{
    :{name} a :Film .
    :{name} :title ?title.
    optional {{ :{name} :duration ?duration.}}
    optional {{ :{name} :description ?description.}}
    optional {{ :{name} :hasDirector ?director.}}
    optional {{ :{name} :hasActor ?actor.}}
    optional {{ :{name} :hasGenre ?genre.}}
    optional {{ :{name} :country ?country.}}
    optional {{ :{name} :hasComposer ?composer.}}
    optional {{ :{name} :hasProducer ?producer.}}
    optional {{ :{name} :hasScreenWriter ?screenwriter.}}
}}
    """
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        dados = tratardados(dados)
        return render_template("filme.html", data = dados)
    else:
        print(resposta.status_code)
        return render_template("empty.html",data = {"data":data_iso_formatada})

@app.route("/realizadores/<string:name>")
def realizador(name):
    sparql_query = f"""
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
SELECT ?filme ?title WHERE {{
    :{name} a :Director.
    ?filme :hasDirector :{name}.
    ?filme :title ?title.
    
}}
    """
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        print(dados)
        return render_template("realizador.html", data = {"dados":dados,"id":name})
    else:
        return render_template("empty.html",data = {"data":data_iso_formatada})

@app.route("/atores/<string:name>")
def ator(name):
    sparql_query = f"""
PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
SELECT ?filme ?title WHERE {{
    :{name} a :Actor.
    ?filme :hasActor :{name}.
    ?filme :title ?title.
    
}}
    """  
    resposta = requests.get(graphdb_endpoint,params = {"query":sparql_query},headers = {"Accept":"application/sparql-results+json"})
    if resposta.status_code == 200:
        dados = resposta.json()["results"]["bindings"]
        return render_template("ator.html", data = {"dados":dados,"id":name})
    else:
        return render_template("empty.html",data = {"data":data_iso_formatada})


if __name__=="__main__":
    app.run(debug=True)