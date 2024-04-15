import json
from rdflib import OWL, Graph, Literal, BNode, Namespace, RDF, URIRef

import xml.etree.ElementTree as ET

g = Graph()
g.parse("familia-base.ttl")

root = ET.parse("biblia.xml")
familia = Namespace("http://rpcw.di.uminho.pt/2024/familia/")
persons_dict = {}
for person in root.findall("person"):
    id = person.find("id").text
    name = person.find("namegiven").text
    sex = person.find("sex").text
    parents = []
    for parent in person.findall("parent"):
        parents.append({"id": parent.get("ref"), "name": parent.text})
    persons_dict[id] = {"name": name, "sex": sex, "parents": parents}
    g.add((URIRef(f"{familia}{id}"), RDF.type, OWL.NamedIndividual))
    g.add((URIRef(f"{familia}{id}"), RDF.type, familia.Pessoa))
    g.add((URIRef(f"{familia}{id}"), familia.nome, Literal(name)))

for person in persons_dict:
    for parent in persons_dict[person]["parents"]:
        if parent["id"] in persons_dict:
            if persons_dict[parent["id"]]["sex"] == "M":
                g.add((URIRef(f"{familia}{person}"), familia.temPai, URIRef(f"{familia}{parent['id']}")))
            elif persons_dict[parent["id"]]["sex"] == "F":
                g.add((URIRef(f"{familia}{person}"), familia.temMae, URIRef(f"{familia}{parent['id']}")))
            else:
                print(f"Parent {parent["id"]} is non binary")
        else: print(f"Parent {parent['id']} not found")


persons_json = json.dumps(persons_dict)
print(g.serialize())
