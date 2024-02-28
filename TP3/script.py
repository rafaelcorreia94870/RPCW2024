import json

f = open("mapa-virtual.json")
bd = json.load(f)
f.close()


ttl = ""
for cidade in bd["cidades"]:
    ttl+=f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{cidade["id"]}
:{cidade["id"]} rdf:type owl:NamedIndividual ,
             :cidade ;
    :descricao "{cidade["descrição"]}" ;
    :distrito "{cidade["distrito"]}" ;
    :id "{cidade["id"]}" ;
    :nome "{cidade["nome"]}" ;
    :populacao {cidade["população"]} .
    """
    
for ligacao in bd["ligacoes"]:
    
    ttl+=f"""
###  http://rpcw.di.uminho.pt/2024/mapa-virtual#{ligacao["id"]}
:{ligacao["id"]} rdf:type owl:NamedIndividual ,
             :ligacao ;
    :destino :{ligacao["destino"]} ;
    :origem :{ligacao["origem"]} ;
    :distancia {ligacao["distância"]} ;
    :id "{ligacao["id"]}" .

"""

with open("caminhos.ttl", "a") as f:
    f.write(ttl)
