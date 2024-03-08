from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

#data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

#GraphDB endpoint
grapdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

@app.route('/')

def index():
    return render_template('index.html', data ={"data":data_iso_formatada})

@app.route('/elementos')
def elementos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT * WHERE {
    ?s a tp:Element;
    tp:name ?nome;
    tp:symbol ?simb;
    tp:atomicNumber ?n .
    ?grupo a tp:Group .
    ?grupo tp:element ?s.
}ORDER BY ?n
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elementos.html', data=dados)
    else:
        return render_template('empty.html', data = data_iso_formatada)
    
@app.route('/grupos')
def grupos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT * WHERE {
    ?s a tp:Group.
    optional{ ?s tp:name ?nome. }
    optional { ?s tp:number ?n . }
}ORDER BY ?n
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('grupos.html', data=dados)
    else:
        return render_template('empty.html', data = data_iso_formatada)

@app.route('/elemento/<int:na>')
def element(na):
    sparql_query = f"""
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT * WHERE {{
    ?s a tp:Element;
    tp:name ?nome;
    tp:symbol ?simb;
    tp:atomicWeight ?pa;
    tp:block ?bloco;
    tp:casRegistryID ?rid;
    tp:classification ?class;
    tp:color ?cor;
    tp:group ?grupo;
    tp:period ?periodo;
    tp:standardState ?estado;
    tp:atomicNumber {na} .
    ?s tp:atomicNumber ?na . 
}}
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        print(dados)
        return render_template('elemento.html', data=dados[0])
    else:
        return render_template('empty.html', data = data_iso_formatada)
    
@app.route('/grupo/<string:na>')
def grupo(na):
    sparql_query = f"""
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT * WHERE {{
    optional {{ tp:{na} tp:name ?nome. }}
    optional{{ tp:{na} tp:number ?n. }}
    tp:{na} tp:element ?element.
    ?element tp:name ?nomeElem .
    ?element tp:symbol ?simb .
    ?element tp:atomicNumber ?na .
    ?element tp:group ?id .
}}
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        print(na)
        print(dados)
        return render_template('grupo.html', data=dados)
    else:
        print(resposta)
        return render_template('empty.html', data = data_iso_formatada)

if __name__ == '__main__':
    app.run(debug=True)