#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:15:39 2026

@author: gustavo
"""

import pandas as pd

chunk_size = 100_000
results = []

#df = pd.read_csv('output/bne.csv.gz', compression='gzip', header=0, skiprows=range(1, 1000000), sep='\t', 
                 #quotechar='"', nrows=10000)

for chunk in pd.read_csv('output/bne-v1.csv.gz', compression='gzip', sep='\t', chunksize=chunk_size):
    # Process each chunk
    print(chunk.dtypes)
    chunk['f001'] = chunk['f001'].apply(str)
    processed = chunk[chunk['f001'].str.len() < 10]
    results.append(processed)

# Combine results if they fit in memory
final_df = pd.concat(results, ignore_index=True)

print(final_df['f001'])