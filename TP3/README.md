Metainformação: TPC3, 28/02/2024, Rafael Correia, RPCW;
Resumo: 
    A partir do dataset criei uma ontologia no Protégé;
        com as classes:
        
    Reusei a script de Python com algumas modificações para povoar a ontologia;
    Criei um novo repositorio no graphDB (mapa-virtual)
    Carreguei a ontologia no GraphDB;

    Queries:
    Quais as cidades de um determinado distrito?
    PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
    select ?nome where { 
        ?s :distrito "Porto" .
        ?s :nome ?nome
    }
    
    Distribuição de cidades por distrito?
    PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
    select ?distrito (COUNT(distinct ?cidade) as ?ncidades) where { 
        ?cidade :distrito ?distrito .
    }
    group by ?distrito

    Quantas cidades se podem atingir a partir do Porto?
    - Diretamente
    PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>

    SELECT distinct ?cidade WHERE {
        ?porto :distrito "Porto" .
        ?ligacao :origem ?porto .
        ?ligacao :destino ?c .
        ?c :nome ?cidade
    }

    Quais as cidades com população acima de um determinado valor?;
    PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>

    SELECT ?nome ?populacao WHERE {
        ?cidade a :cidade .
    	?cidade :nome ?nome .
        ?cidade :populacao ?populacao .
        FILTER (100000 < ?populacao).
    }ORDER BY DESC (?populacao) 

Lista de resultados: caminhos.ttl, script.py.
