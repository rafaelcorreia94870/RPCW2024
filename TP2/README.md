Metainformação: Ontologia de música, 25/02/2024, Rafael Correia, RPCW;
Resumo: 
    - Saquei o Dataset: Escola de Música
    está dividido em
        - alunos
        - instrumentos
        - cursos
    
    - Criei uma ontologia
        - Defeni as classes
            - aluno
            -instrumentos
            -curos
        - com as relações entre o instrumento e o aluno, o instrumento e o curso e o aluno e o curso
        - nas datas properties é igual só que nos instrumentos usei só o "#text"
    - Criei uma script pra povoar a ontologia (tive cuidade aonde os nomes tinham espaços e não podiam)
    - Criar um repositorio no graphDB com a ontologia
    run -d -p 7200:7200 --name graphdbmusica 6708b71e6ed1   

    O resultado final está nas imagens alunos.png, cursos.png e instrumentos.png

Lista de resultados: script.py, musica.ttl, alunos.png, cursos.png e instrumentos.png.


