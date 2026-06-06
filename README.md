# bne-marc2lod

This project tends to align marc records made available by the National Library of Spain and the Linked Open Data version made available at datos.bne.es. 

This repository is based on the dataset https://datosabiertos.bne.es/catalogo/dataset/catalogo-bibliografico-monografias-modernas1

## Scripts

It reads the marcxml file and creates a csv file: [Marc2CSVparser-bne.py](Marc2CSVparser-bne.py)

Then, for each record, it tries to recover URIs from datos.bne.es: [process-bne.py](process-bne.py) reads the csv file and queries datos.bne.es using the script [sparqBne.py](sparqlBne.py)

## Alignment

To the best of our knowledge, there is no direct connection from marc to LOD. As a result, we studied an alternative approach using the fields title, author and isbn. See, for example:

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bne: <https://datos.bne.es/def/>

SELECT *
WHERE {
  ?work rdf:type bne:C1001.
  ?work  rdfs:label "50 a\u00F1os de memoria" .
  ?work bne:id ?id.
  ?work bne:OP1002 ?exp.
  ?exp bne:OP2001 ?recurso.
  ?recurso bne:P3013 "978-84-690-4694-4".
  OPTIONAL {?work owl:sameAs ?sameAsWork.}
  OPTIONAL {?work bne:OP1001 ?author . ?author rdfs:label "Bas Carbonell, Manuel" . ?author owl:sameAs ?sameAsAuthor .}
  OPTIONAL {?work bne:OP7001 ?subject . ?subject rdfs:label ?subjectName}
 }
LIMIT 100
```
