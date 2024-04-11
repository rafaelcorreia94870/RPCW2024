Lista de cidades, ordenada alfabeticamente pelo nome;
```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
SELECT ?nome WHERE {
    ?cidade a :cidade.
    ?cidade :nome ?nome
}ORDER BY ?nome
```
Distribuição das cidades por distrito: lista de distritos ordenada alfabeticamente em que para
cada um se indica quantas cidades tem;
```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
SELECT ?distrito (COUNT(?cidade) as ?ncidade) WHERE {
    ?cidade a :cidade.
    ?cidade :distrito ?distrito.
}GROUP BY ?distrito
ORDER BY ?distrito
```
Que cidades têm ligações diretas com Braga? (Considera Braga como origem mas também
como destino)
```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
SELECT (COUNT(distinct ?cidade) as ?ligacoesdiretas) WHERE {
    ?braga a :cidade.
    ?braga :nome "Braga".
   	?l a :ligacao.
   	{?l :destino ?braga.
     ?l :origem ?cidade.
    }
 	UNION
    {
        ?l :origem ?braga .
        ?l :destino ?cidade.
    }
   	
}
```
Partindo de Braga, que cidades se conseguem visitar? (Apresenta uma lista de cidades
ordenada alfabeticamente)
```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa-virtual/>
SELECT DISTINCT ?cidades WHERE {
    ?braga a :cidade.
    ?braga :nome "Braga".
   	?l a :ligacao.
	?l :origem ?braga .
	?l :destino ?c.
    ?c :nome ?cidades
   	
}ORDER BY ?cidades
```