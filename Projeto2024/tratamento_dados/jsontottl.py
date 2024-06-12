import json
import re

lines = """
@prefix : <http://www.rpcw.pt/rafa/ontologies/2024/paises/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.rpcw.pt/rafa/ontologies/2024/paises/> .

<http://www.rpcw.pt/rafa/ontologies/2024/paises> rdf:type owl:Ontology .

#################################################################
#    Data properties
#################################################################

###  http://www.rpcw.pt/rafa/ontologies/2024/paises/area
:area rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/capital
:capital rdf:type owl:DatatypeProperty ;
         rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/costa
:costa rdf:type owl:DatatypeProperty ;
       rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/densidade_populacional
:densidade_populacional rdf:type owl:DatatypeProperty ;
                        rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/espetativa_de_vida
:espetativa_de_vida rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/exportacoes
:exportacoes rdf:type owl:DatatypeProperty ;
             rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/gdp
:gdp rdf:type owl:DatatypeProperty ;
     rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/hemisferio
:hemisferio rdf:type owl:DatatypeProperty ;
            rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/importacoes
:importacoes rdf:type owl:DatatypeProperty ;
             rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/lado_em_que_conduz
:lado_em_que_conduz rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/latitude
:latitude rdf:type owl:DatatypeProperty ;
          rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/literacia
:literacia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/longitude
:longitude rdf:type owl:DatatypeProperty ;
           rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/migracao_liquida
:migracao_liquida rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/moeda
:moeda rdf:type owl:DatatypeProperty ;
       rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/mortalidade_infantil
:mortalidade_infantil rdf:type owl:DatatypeProperty ;
                      rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/populacao
:populacao rdf:type owl:DatatypeProperty ;
           rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/suicidios_por_1000
:suicidios_por_1000 rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/taxa_de_mortalidade
:taxa_de_mortalidade rdf:type owl:DatatypeProperty ;
                     rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/taxa_de_natalidade
:taxa_de_natalidade rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/telefones_por_1000
:telefones_por_1000 rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises/temperatura_media
:temperatura_media rdf:type owl:DatatypeProperty ;
                   rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#emissoes_co2
:emissoes_co2 rdf:type owl:DatatypeProperty ;
              rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#medicos_por_mil
:medicos_por_mil rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#racio_sexos
:racio_sexos rdf:type owl:DatatypeProperty ;
             rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#receita_imposto
:receita_imposto rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#taxa_desemprego
:taxa_desemprego rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#taxa_fertilidade
:taxa_fertilidade rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pais .


###  http://www.rpcw.pt/rafa/ontologies/2024/paises#nome
:nome rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pais .

###  http://www.rpcw.pt/rafa/ontologies/2024/paises#flag
:flag rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pais .
                  
###  http://www.rpcw.pt/rafa/ontologies/2024/paises#continente
:continente rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Pais .

#################################################################
#    Classes
#################################################################

###  http://www.rpcw.pt/rafa/ontologies/2024/paises/Pais
:Pais rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################


"""
with open('datasets/countriesInfo.json', encoding='UTF-8') as f:
    data = json.load(f)

    for country, attributes in data.items():
       country_fixed = re.sub(r'(\&|\(|\)|\,)', r'\\\1', country).replace(' ', '_').replace("'", '').replace('.', '')
       nome = "\n".join([f':nome "{nome}";'for nome in attributes["nome"]])
       receita_imposto = attributes.get('receita imposto', '')
       if receita_imposto!='':
            receita_imposto = f':receita_imposto "{receita_imposto}";'
       medicos_por_mil = attributes.get('medicos por mil', '')
       if medicos_por_mil!='':
            medicos_por_mil = f':medicos_por_mil "{medicos_por_mil}";'
       lines += f"""
###  http://www.rpcw.pt/rafa/ontologies/2024/paises#{country_fixed}
:{country_fixed} rdf:type owl:NamedIndividual ,
                      :Pais ;
            {nome}
            :area "{attributes.get('area', '')}" ;
            :capital "{attributes.get('capital', '')}" ;
            :costa "{attributes.get('costa', '')}" ;
            :densidade_populacional "{attributes.get('densidade populacional', '')}" ;
            :espetativa_de_vida "{attributes.get('espetativa de vida', '')}" ;
            :exportacoes "{attributes.get('exportacoes', '')}" ;
            :gdp "{attributes.get('gdp', '')}" ;
            :hemisferio "{attributes.get('hemisferio', '')}" ;
            :importacoes "{attributes.get('importacoes', '')}" ;
            :lado_em_que_conduz "{attributes.get('lado em que conduz', '')}" ;
            :latitude "{attributes.get('latitude', '')}" ;
            :literacia "{attributes.get('literacia', '')}" ;
            :longitude "{attributes.get('longitude', '')}" ;
            :migracao_liquida "{attributes.get('migracao liquida', '')}" ;
            :moeda "{attributes.get('moeda', '')}" ;
            :mortalidade_infantil "{attributes.get('mortalidade infantil', '')}" ;
            :populacao "{attributes.get('populacao', '')}" ;
            :taxa_de_mortalidade "{attributes.get('taxa de mortalidade', '')}" ;
            :taxa_de_natalidade "{attributes.get('taxa de natalidade', '')}" ;
            :telefones_por_1000 "{attributes.get('telefones por 1000', '')}" ;
            :temperatura_media "{attributes.get('temperatura media', '')}" ;
            :emissoes_co2 "{attributes.get('emissoes co2', '')}" ;
            {medicos_por_mil}
            :racio_sexos "{attributes.get('racio sexos', '')}" ;
            {receita_imposto}
            :taxa_desemprego "{attributes.get('taxa desemprego', '')}" ;
            :flag "{attributes.get('flag', '')}" ;
            :continente "{attributes.get('continente', '')}" ;
            :taxa_fertilidade "{attributes.get('taxa fertilidade', '')}" .
"""

with open('datasets/countries.ttl', 'w', encoding='UTF-8') as f:
    f.write(lines)