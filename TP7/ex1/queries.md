Quantos alunos estão registados? (inteiro) 299
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT (COUNT(?s) as ?nAlunos) WHERE {
    ?s a :Aluno
}
```
Quantos alunos frequentam o curso "LCC"? (inteiro) 44
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT (COUNT(?s) as ?nAlunos) WHERE {
    ?s a :Aluno;
    :curso "LCC".
}
```
Que alunos tiveram nota positiva no exame de época normal? (lista ordenada alfabeticamente
por nome com: idAluno, nome, curso, nota do exame);
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT ?idAluno ?nome ?curso ?nota WHERE {
    ?idAluno a :Aluno.
    ?idAluno :curso ?curso.
    ?idAluno :nome ?nome.
    ?exame a :Normal.
    ?idAluno :temExame ?exame.
    ?exame :nota ?nota.
    FILTER(?nota > 9.5)
    
}ORDER BY ?nome

```
Qual a distribuição dos alunos pelas notas do projeto? (lista com: nota e número de alunos que
obtiveram essa nota)
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT ?nota (COUNT(?nota) as ?nalunos) WHERE {
    ?idAluno a :Aluno.
    ?idAluno :nota_projeto ?nota.   
}GROUP BY ?nota
ORDER BY ?nota
```
Quais os alunos mais trabalhadores durante o semestre? (lista ordenada por ordem
decrescente do total: idAluno, nome, curso, total = somatório dos resultados dos TPC)
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT  ?idAluno ?nome ?curso (SUM(?tpc) as ?total) WHERE {
    ?idAluno a :Aluno.
    ?idAluno :nome ?nome.
    ?idAluno :curso ?curso.
    ?idAluno :temtpc ?tpcs.
    ?tpcs :nota ?tpc
 
}GROUPBY ?idAluno ?nome ?curso
ORDER BY DESC(?total)

```
Qual a distribuição dos alunos pelos vários cursos? (lista de cursos, ordenada alfabeticamente
por curso, com: curso, número de alunos nesse curso)
```sql
PREFIX : <http://www.semanticweb.org/35193/ontologies/2024/3/alunos/>
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
SELECT ?curso (COUNT(?curso) as ?nalunos) WHERE {
    ?idAluno a :Aluno.
    ?idAluno :curso ?curso.   
 
}GROUP BY ?curso
ORDER BY ASC(?curso) 
```