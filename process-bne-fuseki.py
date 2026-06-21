#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:17:39 2026

@author: gustavo
"""

import pandas as pd
import sparqlBne as bne
import time

#to limit the number of records read
#df = pd.read_csv('output/bne.csv.gz', compression='gzip', header=0, low_memory=False, skiprows=range(1, 1000), sep='\t', 
#                 quotechar='"', nrows=100000)
#df = pd.read_csv('output/bne.csv.gz', compression='gzip', header=0, low_memory=False, sep='\t', 
 #                quotechar='"')
 
batch_size = 25000

for batch in pd.read_csv('output/bne.csv.gz', compression='gzip', header=0, low_memory=False, sep='\t', 
                quotechar='"', chunksize=batch_size):
    print(f"Processing {len(batch)} rows")

    #print(df)
    #print(df.dtypes)
    
    #print(df.columns.tolist())
    batch["f001"] = batch["f001"].astype(str)
    # init dataframe matching records
    dfBne = pd.DataFrame()
    
    for index, row in batch.iterrows():
        #print(f"Index: {index}, : {row['f020a']}, Utitle: {row['f240a']}, title: {row['f245a']}, author: {row['f100a']}")
        
        # params
        title = ''
        if not pd.isna(row['f240a']):
            title = row['f240a']
        else:
            title = row['f245a']
     
        
        author = ''
        if not pd.isna(row['f100a']):
            if "#" in row['f100a']:
                authors = list(dict.fromkeys(row['f100a'].split("#")))
                author = authors[0]
            else:
                author = row['f100a']
    
        
        isbn = ''
        if not pd.isna(row['f020a']):
            isbn = row['f020a']
    
        
        params = {
        "title": title,
        "isbn": isbn,
        "author": author
        }
        print(params)
        
        #P1011 etiqueta asociada al autor en manifestation
        #https://datos.bne.es/resource/bimo0001420064.ttl
        #https://datos.bne.es/obra/XX1996894.html
        
        query = ''
        
        query ="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX bne: <https://datos.bne.es/def/> 
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            SELECT *
            WHERE {{ 
               ?recurso rdfs:label ?title .
               #BIND(LCASE("{title}") AS ?pTitle) .
               #FILTER(CONTAINS(LCASE(STR(?title)), ?pTitle))
               ?recurso bne:id ?id . 
               #?work bne:OP1002 ?exp . 
               #?exp bne:OP2001 ?recurso . 
               #OPTIONAL {{?work owl:sameAs ?sameAsWork}} . 
               #OPTIONAL {{?work bne:OP7001 ?subject . ?subject rdfs:label ?subjectName}} .
               """
        if not pd.isna(row['f020a']):
            query += '?recurso bne:P3013 "{isbn}" . ' 
        
        #if author != '':
            #query += "OPTIONAL {{?work bne:OP1001 ?author . ?author rdfs:label '{author}' . OPTIONAL {{?author owl:sameAs ?sameAsAuthor}} }}. "
        query += "}} LIMIT 5"
        query = query.format(**params)
       
           
        print(index)
        #if index <= 1: 
        #    pass
        #elif index > 1 and index < 100000:
            #print(query)
            #print(pd.isna(row["f100a"]))
            
        try:
            if not pd.isna(row['f020a']):
                #print(query)
                data_extracter = bne.BNEQueryResults(query)
                #time.sleep(5) 
                dfrecord = data_extracter.load_as_dataframe()
                dfrecord["idmarc"] = str(row["f001"])
                #print(dfrecord.head())
                if len(dfrecord.index) > 0:
                    dfBne = pd.concat([dfBne, dfrecord], ignore_index=True)
               
        except Exception as e:
            print(e)
            print("Error:" + str(row["f001"]))
        #else: break
    print(dfBne)
    dfBne.to_csv("bne-matching.csv", mode="a", #append
                  header=False,  # don't write header again
                  index=False)