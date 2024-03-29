Metainformação: App cinema, 29/03/2024, Rafael Picão Ferreira Correia, RPCW;

Resumo: 
    1. Carregar o dataset no endpoint 'http://epl.di.uminho.pt:7200',
    no repositório 'http://epl.di.uminho.pt:7200/repositories/cinema2024'
    2. Construir queires SPARQL para responder às perguntas:
        

        ---

        1. Quantos filmes existem no repositório?

        ```sql

        PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
        select (COUNT(?s) as ?nfilmes) where {
            ?s a :Film .
        }

        ```


        2. Qual a distribuição de filmes por ano de lançamento?



        ```sql
        ...

        ```

        3. Qual a distribuição de filmes por género?



        ```sql

        PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
        select ?genre (COUNT(?s) as ?nfilmes) where {
            ?s a :Film .
            ?s :hasGenre ?genre.
        } 
        GROUP BY (?genre)
        ORDER BY DESC (?nfilmes)

        ```

        4. Em que filmes participou o ator "Burt Reynolds"?


        ```sql

        PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
        select ?s where {
            ?s a :Film .
            ?s :hasActor :Burt_Reynolds.
        } 


        ```

        5. Produz uma lista de realizadores com o seu nome e o número de filmes que realizou.


        ```sql

        PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
        select ?director (COUNT(?s) as ?nfilmes) where {
            ?s a :Film .
            ?s :hasDirector ?director.
        } 
        GROUP BY (?director)
        ORDER BY DESC (?nfilmes)


        ```

        6. Qual o título dos livros que aparecem associados aos filmes?


        ```sql
        ...

        ```






        ---

    3. Usar o flask para gerar uma interface web ao repositório de filmes (obrigatório usar o endpoint definido ao início).



Lista de resultados: out.ttl, app_cinema/, script.py.

