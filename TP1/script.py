import json

ruas = set()
plantas = set()
f = open("plantas.json")

bd = json.load(f)

f.close()
ttl=""
for obj in bd:
    registo = ""
    if obj['Id'] not in plantas and not obj['Id'] == '':
        plantas.add(obj['Id'])
        registo = f"""

        ###  http://rpcw.di.uminho.pt/2024/plantas#planta_{obj['Id']}
:planta_{obj['Id']} rdf:type owl:NamedIndividual ;
                 :tem_rua :rua_{obj['Código de rua']} ;
                 :caldeira "{obj['Caldeira']}" ;
                 :data_de_atualizacao "{obj['Data de actualização']}" ;
                 :data_de_plantacao "{obj['Data de Plantação']}" ;
                 :especie "{obj["Espécie"]}" ;
                 :estado "{obj["Estado"]}" ;
                 :gestor "{obj["Gestor"]}" ;
                 :id {obj['Id']} ;
                 :implantacao "{obj["Implantação"]}" ;
                 :nome_cientifico "{obj["Nome Científico"]}" ;
                 :numero_de_intervencoes {obj["Número de intervenções"] if obj["Número de intervenções"]!="" else 0 } ;
                 :numero_de_registo {obj["Número de Registo"]} ;
                 :origem "{obj["Origem"]}" ;
                 :tutor "{obj["Tutor"]}" .

        """
    if obj['Código de rua'] not in ruas and not obj['Código de rua'] == '':
        ruas.add(obj['Código de rua'])
        aux = obj["Rua"].replace('"', '\\"')
        registo+=f"""

###  http://rpcw.di.uminho.pt/2024/plantas#rua_{obj['Código de rua']}
:rua_{obj['Código de rua']} rdf:type owl:NamedIndividual ;
             :tem_planta :planta_{obj["Id"]} ;
             :codigo_de_rua {obj['Código de rua']} ;
             :freguesia "{obj['Freguesia']}" ;
             :local "{obj["Local"]}" ;
             :rua "{aux}" .
             
        """

    ttl+=registo

with open("planta.ttl","a") as f2:
    f2.write(ttl)
