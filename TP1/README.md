Metainformação: TPC1: Convertor de TTL, 12/02/2024, Rafael Correia, RPCW

Resumo: 

    Etapa 1 analizar o dataset

    Apos analizar vi que podiamos dividi-lo em duas classes:
    Plantas e Ruas

    Aonde as Ruas teriam as características Código de rua, Rua, Local, Freguesia
    e as Plantas teriam as caracterísitcas Id, Número de Registo, Espécie, Nome Científico, Origem, Data de Plantação, Estado, Caldeira, Tutor, Implantação, Gestor, Data de actualização, Número de intervenções

    Criei uma instancia de rua e uma instancia de planta e vi o ficheiro criado

    Criei um script com base no ficheiro criado e no script da aula.

    Reparei que o dataset tinha bastante lixo:
        A rua usava '"' entao fiz isto: obj["Rua"].replace('"', '\\"') e meti na string o resultado
        Tambem havia casos aonde nao havia o numero da rua ou o Id da planta pro isso nao inclui esses casos., Data, Autor, UC;
        Mudei manulamente os sitios aonde no numero_de_intervencoes tinha uma data para 0.


Lista de resultados: planta.ttl, script.py.