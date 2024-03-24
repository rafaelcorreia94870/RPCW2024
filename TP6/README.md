Metainformação: Título, Data, Autor, UC;
Resumo: Lista de parágrafos;
Lista de resultados: ficheiros.

## TPC6 Cinema et all:

1. Carregar o dataset no endpoint 'http://epl.di.uminho.pt:7200',
no repositório 'http://epl.di.uminho.pt:7200/repositories/cinema2024'
2. Construir queires SPARQL para responder às perguntas:
    - Quantos filmes existem no repositório?
    - Qual a distribuição de filmes por ano de lançamento?
    - Qual a distribuição de filmes por género?
    - Em que filmes participou o ator "Bur Reynolds"?
    - Produz uma lista de realizadores com o seu nome e o número de filmes que realizou.
    - Qual o título dos livros que aparecem associados aos filmes?
3. Usar o flask para gerar uma interface web ao repositório de filmes (obrigatório usar o endpoint definido ao início).