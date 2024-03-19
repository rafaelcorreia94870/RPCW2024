Metainformação: Fazer um Json de Filmes , 16/03/2024, Rafael Correia, RPCW;

Resumo: Lista de parágrafos;
    Fui ao schema.org analizar o dbo:Film
    Vi que o nome, o abstract e a duração eram as únicas coisas que não iriam ter múltiplas entradas (se filtrarmos por lingua)

    Achei as seguintes características relevantes:
        atores -> dpo:starring -> rdfs:label
        musicos -> dbo:musicComposer -> dbp:name
        realizadores ->  dbp:director 
        produtores = dbo:producer -> dbp:name 
        paises -> dbp:country 
        generos -> dbp:Genre 
        escritores -> dbp:writer
    também achei o budget importante mas tinha múltiplos tipos, desde um double, até o tipo dollar e Pound, etc.

    No filmes.json tem todos os filmes apenas com o uri, nome, duração e descrição.
    No filme mais info meti tudo, só que não corri para os primeiros 5 por questões de duração do programa.

    Numa segunda iteração deste TPC tentei fazer tudo num só request, e pedi-a multiplas vezes com um offset de maneira a ter a informação toda, mas por alguma razão a script não é consistento no seu output.

    

Lista de resultados: getFilmes.py, getBuedaCenas.py, filmes.json, filmesMaisInfo.json, filmes2.json.