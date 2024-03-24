from rdflib import Graph,URIRef,Literal,Namespace
from rdflib.namespace import RDF,OWL
import json

g = Graph()

g.parse("cinema.ttl")



""" 



"""
filmes=[]
cinema = Namespace("http://rpcw.di.uminho.pt/2024/cinema/")
with open("movies.json","r") as f:
    filmes = json.load(f)
    
for filme in filmes:
    filme["movie"] = filme["movie"].replace(" ", "_")
    filme["movie"] = filme["movie"].replace("\"", "")
    g.add((URIRef(f"{cinema}{filme["movie"]}"),RDF.type,OWL.NamedIndividual))
    g.add((URIRef(f"{cinema}{filme["movie"]}"),RDF.type,cinema.Film)) 
    g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.title,Literal(filme["movie"])))
    #description
    if filme["description"]:
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.description,Literal(filme["description"][0])))
    #duration, its optional
    if "duration" in filme:
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.duration,Literal(filme["duration"])))

    for actor in filme["actors"]:
        actor = actor.replace(" ", "_")
        actor = actor.replace("\"", "")
        actor = actor.split("\n")[0]
        actor = actor.replace("|", "_")
        g.add((URIRef(f"{cinema}{actor}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{actor}"),RDF.type,cinema.Actor)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasActor,cinema.Film)) 
    for director in filme["directors"]:
        director = director.replace(" ", "_")
        director = director.replace("\"", "")
        director = director.split("\n")[0]
        g.add((URIRef(f"{cinema}{director}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{director}"),RDF.type,cinema.Director)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasDirector,cinema.Director))
    for genre in filme["genre"]:
        genre = genre.replace(" ", "_")
        genre = genre.replace("\"", "")
        g.add((URIRef(f"{cinema}{genre}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{genre}"),RDF.type,cinema.Genre)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasGenre,cinema.Genre))
    for countrys in filme["country"]:
        countrys = countrys.replace("\n", ",")
        countries = countrys.split(",\n")
        for country in countries:
            country = country.replace(" ", "_")
            country = country.replace("\"", "") 
            g.add((URIRef(f"{cinema}{country}"),RDF.type,OWL.NamedIndividual))
            g.add((URIRef(f"{cinema}{country}"),RDF.type,cinema.Country)) 
            g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasCountry,cinema.Country))
    for producer in filme["producers"]:
        producer = producer.replace(" ", "_")
        producer = producer.replace("\"", "") 
        g.add((URIRef(f"{cinema}{producer}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{producer}"),RDF.type,cinema.Producer)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasProducer,cinema.Producer))
    for writer in filme["writers"]:
        writer = writer.replace(" ", "_")
        writer = writer.replace("\"", "")
        g.add((URIRef(f"{cinema}{writer}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{writer}"),RDF.type,cinema.Writer)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasWriter,cinema.Writer))
    for composer in filme["composers"]:
        composer = composer.replace(" ", "_")
        composer = composer.replace("\"", "")
        g.add((URIRef(f"{cinema}{composer}"),RDF.type,OWL.NamedIndividual))
        g.add((URIRef(f"{cinema}{composer}"),RDF.type,cinema.Musician)) 
        g.add((URIRef(f"{cinema}{filme["movie"]}"),cinema.hasComposer,cinema.Musician))
    
    
    
        
    



#print(len(g))
print(g.serialize())

# print("=====================================")
# import pprint
# for stmt in g:
#     pprint.pprint(stmt)