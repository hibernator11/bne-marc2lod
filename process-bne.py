#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:17:39 2026

@author: gustavo
"""

import pandas as pd
import sparqlBne as bne
import time

df = pd.read_csv('output/bne-v1.csv.gz', compression='gzip', header=0, low_memory=False, skiprows=range(1, 1000), sep='\t', 
                 quotechar='"', nrows=100000)

print(df)
print(df.dtypes)

print(df.columns.tolist())

for index, row in df.iterrows():
    print(f"Index: {index}, : {row['f020a']}, title: {row['f245a']}, author: {row['f100a']}")
    
    params = {
    "title": row['f245a'],
    "isbn": row['f020a'],
    "author": row['f100a']
    }
    
    query ="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX bne: <https://datos.bne.es/def/> 
            SELECT * 
            WHERE {{ 
               ?work rdf:type bne:C1001. 
               ?work rdfs:label "{title}" . 
               ?work bne:id ?id. 
               ?work bne:OP1002 ?exp. 
               ?exp bne:OP2001 ?recurso. 
               ?recurso bne:P3013 "{isbn}". 
               OPTIONAL {{?work owl:sameAs ?sameAsWork.}} 
               OPTIONAL {{?work bne:OP1001 ?author . ?author rdfs:label "{author}" . ?author owl:sameAs ?sameAsAuthor .}} 
               OPTIONAL {{?work bne:OP7001 ?subject . ?subject rdfs:label ?subjectName}} 
           }} 
           LIMIT 5""".format(**params)
    print(query)
    print(pd.isna(row["f100a"]))
    
    try:
       data_extracter = bne.BNEQueryResults(query)
       time.sleep(3) 
       dfBne = data_extracter.load_as_dataframe()
       print(dfBne.head())
       if len(dfBne.index) > 0:
           dfBne.to_csv(str(row["f001"]) + '-df.csv')
    except:
        print("Error:" + str(row["f001"]))
    
    print(index)
    if index == 50:
        break
