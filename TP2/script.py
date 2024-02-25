import json

alunos = set()
cursos = set()
instrumentos = set()

f = open("db.json")

bd = json.load(f)

f.close()
ttl='''
#################################################################
#    Individuals
#################################################################

'''

for instrumento in bd["instrumentos"]:
    instrumento["#text"] = instrumento["#text"].replace(" ","_")

    ttl += f'''

###  http://rpcw.di.uminho.pt/2024/musica#{instrumento["#text"]}
:{instrumento["#text"]} rdf:type owl:NamedIndividual ,
                    :Instrumento ;
           :nomeDoInstrumento "{instrumento["#text"]}" .

'''

for curso in bd["cursos"]:
    curso["id"] = curso["id"].replace(" ", "_")

    ttl+= f'''

    ###  http://rpcw.di.uminho.pt/2024/musica#{curso["id"].replace(" ", "_")}
:{curso["id"].replace(" ", "_")} rdf:type owl:NamedIndividual ,
              :Curso ;
     :ensinaInstrumento :{curso["instrumento"]["#text"].replace(" ","_")} ;
     :cursoDesignacao "{curso["designacao"].replace(" ","_")}" ;
     :cursoDuracao "{curso["duracao"].replace(" ","_")}" .
     
'''
    
for aluno in bd["alunos"]:
    ttl+=f'''

###  http://rpcw.di.uminho.pt/2024/musica#{aluno["id"].replace(" ","_")}
:{aluno["id"].replace(" ","_")} rdf:type owl:NamedIndividual ,
                :Aluno ;
       :temInstrumento :{aluno["instrumento"].replace(" ","_")} ;
       :temcurso :{aluno["curso"].replace(" ","_")} ;
       :alunoId "{aluno["id"].replace(" ","_")}" ;
       :anoCurso "{aluno["anoCurso"].replace(" ","_")}" ;
       :dataNasc "{aluno["dataNasc"].replace(" ","_")}" ;
       :nomeAluno "{aluno["nome"].replace(" ","_")}" .

'''

with open("musica.ttl","a") as f2:
    f2.write(ttl)
