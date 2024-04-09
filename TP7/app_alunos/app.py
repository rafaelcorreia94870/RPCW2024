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
SELECT ?nome WHERE {{
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
"""
        elif request.args["groupBy"] == "recurso":
            """
            GET /api/alunos?groupBy=recurso - Devolve a lista de alunos, ordenada
            alfabeticamente por nome, que realizaram o exame de recurso: idAluno, nome, curso, recurso;
            """
            sparql_query = """
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
SELECT * WHERE {
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
    :temtpc ?tpcs;
    :nota_projeto ?nota_projeto;
    :temExame ?exame .
    ?exame :nota ?notasexames.
	?tpcs :nota ?notatpcs.    
}}
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        for dado in dados:
           for key, value in dado.items():
               dado[key] = value['value']
        return dados
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
    :temtpc ?tpcs;
    :nota_projeto ?nota_projeto;
    :temExame ?exame .
    ?exame :nota ?notasexames.
	?tpcs :nota ?notatpcs.    
}ORDER BY ?nome
"""
    resposta = requests.get(grapdb_endpoint, params={"query":sparql_query}, headers={'Accept' :'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        for dado in dados:
           for key, value in dado.items():
               dado[key] = value['value']
               if key == "nota_projeto" and float(dado[key]) < 10:
                    dado["notaFinal"] = "R"
        #calcular nota final e ter só ?idAluno ?nome ?curso ?notaFinal no json
        for dado in dados:
            if "notaFinal" not in dado:
                notaFinal = 0
                for key, value in dado.items():
                    if key == "notasexames":
                        if float(value) > notaFinal:
                            notaFinal = float(value)
                    elif key == "notatpcs":
                        notaFinal += float(value)
                    elif key == "nota_projeto":
                        nota_projeto = float(value)
                notaFinal = notaFinal + (nota_projeto * 0.4) + (notaFinal * 0.4)
                if notaFinal < 10:
                    dado["notaFinal"] = "R"
                else:
                    dado["notaFinal"] = notaFinal
        return dados
    else:
        return "ERROR: Não foi possível aceder aos dados dos alunos avaliados."
    
if __name__ == '__main__':
    app.run(debug=True)