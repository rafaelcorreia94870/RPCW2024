from flask import Flask, render_template, url_for, request
from datetime import datetime
import requests

app = Flask(__name__)

#data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

#GraphDB endpoint
grapdb_endpoint = "http://localhost:7200/repositories/alunos"

"""
FUNÇÃO CUJO OBJETIVO É ORGANIZAR UM ALUNO UM UNICO OBJETO JSON
"""
def tratarAluno(dados, id):
    aluno = {}
    exames = {}
    tpcs = {}
    aluno["nome"] = dados[0]["nome"]["value"]
    aluno["curso"] = dados[0]["curso"]["value"]
    aluno["idAluno"] = id
    aluno["nota_projeto"] = dados[0]["nota_projeto"]["value"]
    for linha in dados:
        exame = linha["exame"]["value"].split("_")[-1]
        tpc = linha["tpc"]["value"].split("_")[-1]
        if exame not in exames:
            exames[exame] = linha["notasexames"]["value"]
        if tpc not in tpcs:
            tpcs[tpc] = linha["notatpcs"]["value"]
    aluno["exames"] = exames
    aluno["tpcs"] = tpcs
    
    return aluno

"""
FUNÇÃO CUJO OBJETIVO É AVALIAR OS ALUNOS
"""
def avaliarAlunos(dados):
    alunos = {}
    for linha in dados:
        idAluno = linha["idAluno"]["value"]
        if idAluno not in alunos:
            alunos[idAluno] = {}
        if "nome" not in alunos[idAluno]:
            alunos[idAluno]["nome"] = linha["nome"]["value"]
        if "curso" not in alunos[idAluno]:
            alunos[idAluno]["curso"] = linha["curso"]["value"]
        if "nota_projeto" not in alunos[idAluno]:
            alunos[idAluno]["notaProjeto"] = float(linha["nota_projeto"]["value"])
        if "exames" not in alunos[idAluno]:
            alunos[idAluno]["exames"] = {}
        if "tpcs" not in alunos[idAluno]:
            alunos[idAluno]["tpcs"] = {}
        exame = linha["exame"]["value"].split("_")[-1]
        tpc = linha["tpc"]["value"].split("_")[-1]
        if exame not in alunos[idAluno]["exames"]:
            alunos[idAluno]["exames"][exame] = float(linha["notasexames"]["value"])
        if tpc not in alunos[idAluno]["tpcs"]:
            alunos[idAluno]["tpcs"][tpc] = float(linha["notatpcs"]["value"])
    for aluno in alunos:
        notaFinal = 0
        if alunos[aluno]["notaProjeto"] < 10:
            notaFinal = "R"
        else:
            notaExame = max(alunos[aluno]["exames"].values())
            if (notaExame) < 10:
                notaFinal = "R"
            else:
                for tpc in alunos[aluno]["tpcs"]:
                    notaFinal += alunos[aluno]["tpcs"][tpc]
                notaFinal += 0.4*alunos[aluno]["notaProjeto"]
                notaFinal += 0.4*notaExame
                if notaFinal < 10:
                    notaFinal = "R"
                else:
                    notaFinal = round(notaFinal,2)
        alunos[aluno]["notaFinal"] = notaFinal
        alunos[aluno].pop("exames")
        alunos[aluno].pop("tpcs")
    return alunos
"""
GET /api/alunos - Devolve a lista dos alunos, ordenada alfabeticamente por nome, com os
campos: idAluno, nome e curso;
"""
@app.route('/api/alunos')
def alunos():
    if "curso" in request.args:
        """
        GET /api/alunos?curso=X - Devolve apenas uma lista, ordenada alfabeticamente por
        nome, com os alunos do curso X;
        """
        sparql_query = f"""
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?idALuno ?nome WHERE {{
    ?idALuno a :Aluno;
    :nome ?nome;
    :curso "{request.args['curso']}" .
}}ORDER BY ?nome
"""
    elif "groupBy" in request.args:
        if request.args["groupBy"] == "curso":
            """
            GET /api/alunos?groupBy=curso - Devolve a lista de cursos, ordenada alfabeticamente,
            e para cada um indica quantos alunos estão registados;
            """    
            sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?curso (COUNT(?curso) as ?total) WHERE {
    ?idALuno a :Aluno;
    :curso ?curso .
}GROUP BY ?curso
"""
            
        elif request.args["groupBy"] == "projeto":
            """
            GET /api/alunos?groupBy=projeto - Devolve uma lista de notas registadas no projeto e
            para cada um indica o total de alunos que a obtiveram;
            """
            sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?nota (COUNT(?nota) as ?total_alunos) WHERE {
    ?idALuno a :Aluno;
    :nota_projeto ?nota .
}GROUP BY ?nota
ORDER BY ?nota
"""
        elif request.args["groupBy"] == "recurso":
            """
            GET /api/alunos?groupBy=recurso - Devolve a lista de alunos, ordenada
            alfabeticamente por nome, que realizaram o exame de recurso: idAluno, nome, curso, recurso;
            """
            sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?idALuno ?nome ?curso ?notasexame WHERE {
    ?idALuno a :Aluno;
    :nome ?nome;
    :curso ?curso;
    :temExame ?exame .
    ?exame a :Recurso .
    ?exame :nota ?notasexame.
}ORDER BY ?nome
"""
    else:
        sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?idAluno ?nome ?curso WHERE {
    ?idAluno a :Aluno;
    :nome ?nome;
    :curso ?curso .	
}ORDER BY ?nome
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        for dado in dados:
           for key, value in dado.items():
               dado[key] = value['value']
        return dados
    else:
        return "ERROR: Não foi possível aceder aos dados dos alunos."
    
"""
GET /api/alunos/:id - Devolve a informação completa de um aluno (nesta rota, considere
para id o campo idAluno);
"""

@app.route('/api/alunos/<string:id>')
def aluno(id):
    sparql_query = f"""
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT * WHERE {{
    :{id} a :Aluno;
    :nome ?nome;
    :curso ?curso;
    :temtpc ?tpc;
    :nota_projeto ?nota_projeto;
    :temExame ?exame .
    ?exame :nota ?notasexames.
	?tpc :nota ?notatpcs.    
}}
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        
        organizado = tratarAluno(dados,id)
        return organizado
    else:
        return "ERROR: Não foi possível aceder aos dados do aluno."


"""
GET /api/alunos/tpc - Devolve a lista de alunos (com idAluno, nome e curso), ordenada
alfabeticamente por nome, e um quarto campo correspondente ao número de TPC realizados;
"""
@app.route('/api/alunos/tpc')
def tpc():
    sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT ?idAluno ?nome ?curso (COUNT(?tpc) as ?ntpcs) WHERE {
    ?idAluno a :Aluno;
    :nome ?nome;
    :curso ?curso;
    :temtpc ?tpc .
}GROUP BY ?idAluno ?nome ?curso
ORDER BY ?nome 
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
            
        for dado in dados:
           for key, value in dado.items():
               dado[key] = value['value']
        return dados
    else:
        return "ERROR: Não foi possível aceder aos dados dos alunos com TPCs."
    
    
"""
GET /api/alunos/avaliados - Devolve uma lista de alunos, ordenada alfabeticamente por
nome, com o resultado final: idAluno, nome, curso e notaFinal, em que notaFinal poderá ser
"R" ou um valor entre 10 e 20 calculado da seguinte forma:
Se a nota do Projeto for inferior a 10 o resultado é "R";

Se o máximo das notas obtidas em exame for inferior a 10 o resultado é "R";

A nota final é calculada somando todos os resultados obtidos nos TPC, e somando a
este resultado 40% da nota do projeto e 40% da nota máxima obtida em exame;
se esta nota final for inferior a 10 o resultado é "R" caso contrário o resultado é a nota calculada"""

@app.route('/api/alunos/avaliados')
def avaliados():
    sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT * WHERE {
    ?idAluno a :Aluno;
    :nome ?nome;
    :curso ?curso;
    :temtpc ?tpc;
    :nota_projeto ?nota_projeto;
    :temExame ?exame .
    ?exame :nota ?notasexames.
	?tpc :nota ?notatpcs.  
}ORDER BY ?nome
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        organizado = avaliarAlunos(dados)
        return organizado
    else:
        return "ERROR: Não foi possível aceder aos dados dos alunos avaliados."
    
if __name__ == '__main__':
    app.run(debug=True)