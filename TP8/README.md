Metainformação: Carregar um dataset numa ontologia, 15/04/2024, Rafael Picão Ferreira Correia, RPCW;

Resumo: 
    Observei os datasets, vi que a biblia.xml parecia mais limpo

    Carreguei o dataset pra um dicionario com o id, nome sexo e pais. (Adicionei na ontologia imediatamente o id e o nome)

    Depois de carregar o dataset pra um dicionario percorri cada pessoa e para cada parente que ele tinha, via o sexo com que guardei o parente. se fosse M, teria a relação temPai, se fosse F, teria a relaçao temMae. Meti caso não tivesse pais, daria erro. Como não teve erro, não tive que guardar os filhos de cada pessoa e ver as relações ai também.

Lista de resultados: novo.ttl, addToOnt.py.

