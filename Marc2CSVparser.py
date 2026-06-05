#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:29:11 2022

@author: gustavo
"""
import xml.sax
import pandas as pd

#Global list variable to keep track of rows of nmap data to be written to CSV
rowsList = []

class MARC_Handler(xml.sax.ContentHandler):
    
    def __init__(self):
        global rowsList
        self.key = None
        self.text = ''
        self.parent = ''
        
        self.f001 = None
        self.f020a = None        
        self.f040b = None
        self.f100a = ''
        self.f100e = ''
        self.f245a = None
        self.f245b = None
        self.f245c = None
        self.f245n = None
        self.f245p = None
        self.f246a = ''
        self.f263a = ''
        self.f264a = None
        self.f264b = None
        self.f264c = None
        self.f300a = None
        self.f300b = None
        self.f300c = None
        self.f336a = None
        self.f338a = None
        self.f347a = None
        self.f347b = None
        self.f490a = None
        self.f500a = None
        self.f504a = None
        self.f588a = None
        self.f600a = ''
        self.f600d = ''
        self.f6001 = ''
        self.f650a = ''
        self.f650x = ''
        self.f650z = ''
        self.f651a = ''
        self.f651x = ''
        self.f700a = ''
        self.f700c = ''
        self.f700d = ''
        self.f710a = ''
        self.f720a = ''
        self.f776i = None
        self.f776z = None
        self.f830a = None
        
    def startElement(self, tag, attributes):
        #print('startelement:' + tag)
        if 'tag' in attributes.keys():
            self.key = attributes.get('tag')
            self.parent = self.key
        elif 'code' in attributes.keys():
            self.key = attributes.get('code')
                        
    def endElement(self, tag):
        #print('endelement:' + tag + " " + self.text)
        if tag == "controlfield" and self.key == "001":
            self.f001 = self.text
        
        if tag == "record":
            
            if self.f100a.endswith('#'): self.f100a = self.f100a[:-1]
            if self.f100e.endswith('#'): self.f100e = self.f100e[:-1]
            if self.f246a.endswith('#'): self.f246a = self.f246a[:-1]
            if self.f263a.endswith('#'): self.f263a = self.f263a[:-1]
            if self.f600a.endswith('#'): self.f600a = self.f600a[:-1]
            if self.f600d.endswith('#'): self.f600d = self.f600d[:-1]
            if self.f6001.endswith('#'): self.f6001 = self.f6001[:-1]
            if self.f650a.endswith('#'): self.f650a = self.f650a[:-1]
            if self.f650x.endswith('#'): self.f650x = self.f650x[:-1]
            if self.f650z.endswith('#'): self.f650z = self.f650z[:-1]
            if self.f651a.endswith('#'): self.f651a = self.f651a[:-1]
            if self.f651x.endswith('#'): self.f651x = self.f651x[:-1]
            if self.f700a.endswith('#'): self.f700a = self.f700a[:-1]
            if self.f700c.endswith('#'): self.f700c = self.f700c[:-1]
            if self.f700d.endswith('#'): self.f700d = self.f700d[:-1]
            if self.f710a.endswith('#'): self.f710a = self.f710a[:-1]
            if self.f720a.endswith('#'): self.f720a = self.f720a[:-1]
            
            rowsList.append([self.f001, self.f020a, self.f040b, self.f100a, self.f100e, 
                             self.f245a, self.f245b, self.f245c, 
                             self.f245n, self.f245p, 
                             self.f246a, self.f263a, 
                             self.f264a, self.f264b, self.f264c, 
                             self.f300a, self.f300b, self.f300c, 
                             self.f336a, self.f338a, self.f347a, 
                             self.f347b, self.f490a, self.f504a, self.f500a, self.f588a,
                             self.f600a, self.f600d, self.f6001,
                             self.f651a, self.f651x, self.f650a, self.f650x, self.f650z, 
                             self.f700a, self.f700c, self.f700d,
                             self.f710a, self.f720a, 
                             self.f776i, self.f776z, self.f830a])
            self.f001 = None
            self.f020a = None
            self.f040b = None
            self.f100a = ''
            self.f100e = ''
            self.f245a = None
            self.f245b = None
            self.f245c = None
            self.f245n = None
            self.f245p = None
            self.f246a = ''
            self.f263a = ''
            self.f264a = None
            self.f264b = None
            self.f264c = None
            self.f300a = None
            self.f300b = None
            self.f300c = None
            self.f336a = None
            self.f338a = None
            self.f347a = None
            self.f347b = None
            self.f490a = None
            self.f500a = None
            self.f504a = None
            self.f588a = None
            self.f600a = ''
            self.f600d = ''
            self.f6001 = ''
            self.f651a = ''
            self.f651x = ''
            self.f650a = ''
            self.f650x = ''
            self.f650z = ''
            self.f700a = ''
            self.f700c = ''
            self.f700d = ''
            self.f710a = ''
            self.f720a = ''
            self.f776i = None
            self.f776z = None
            self.f830a = ''
        
        if self.parent == '020':
            if self.key == 'a':
                self.f020a = self.text
        elif self.parent == '040':
            if self.key == 'b':
                self.f040b = self.text
        elif self.parent == '100':
            if self.key == 'a' and self.text != '':
                self.f100a += self.text + '#'
            elif self.key == 'e' and self.text != '':
                self.f100e += self.text + '#'
        elif self.parent == '245':
            if self.key == 'a':
                self.f245a = self.text
            elif self.key == 'b':
                self.f245b = self.text
            elif self.key == 'c':
                self.f245c = self.text
            elif self.key == 'n':
                self.f245n = self.text
            elif self.key == 'p':
                self.f245p = self.text
        elif self.parent == '263':
            if self.key == 'a' and self.text != '':
                self.f263a += self.text + '#'
        elif self.parent == '246':
            if self.key == 'a' and self.text != '':
                self.f246a += self.text + '#'
        elif self.parent == '264':
            if self.key == 'a':
                self.f264a = self.text
            elif self.key == 'b':
                self.f264b = self.text
            elif self.key == 'c':
                self.f264c = self.text
        elif self.parent == '300':
            if self.key == 'a':
                self.f300a = self.text
            elif self.key == 'b':
                self.f300b = self.text
            elif self.key == 'c':
                self.f300c = self.text
        elif self.parent == '336':
            if self.key == 'a':
                self.f336a = self.text
        elif self.parent == '338':
            if self.key == 'a':
                self.f338a = self.text
        elif self.parent == '347':
            if self.key == 'a':
                self.f347a = self.text
        elif self.parent == '347':
            if self.key == 'b':
                self.f347b = self.text
        elif self.parent == '490':
            if self.key == 'a':
                self.f490a = self.text
        elif self.parent == '500':
            if self.key == 'a':
                self.f500a = self.text
        elif self.parent == '504':
            if self.key == 'a':
                self.f504a = self.text
        elif self.parent == '588':
            if self.key == 'a':
                self.f588a = self.text
        elif self.parent == '600':
            if self.key == 'a' and self.text != '':
                self.f600a += self.text + '#'
            elif self.key == 'd' and self.text != '':
                self.f600d += self.text + '#'
            elif self.key == '1' and self.text != '':
                self.f6001 += self.text + '#'                
        elif self.parent == '650':
            if self.key == 'a' and self.text != '':
                self.f650a += self.text + '#'
            elif self.key == 'x' and self.text != '' :
                self.f650x += self.text + '#'
            elif self.key == 'z' and self.text != '':
                self.f650z += self.text + '#'
        elif self.parent == '651':
            if self.key == 'a' and self.text != '':
                self.f651a += self.text + '#'
            elif self.key == 'x' and self.text != '':
                self.f651x += self.text + '#'
        elif self.parent == '700':
            if self.key == 'a' and self.text != '':
                self.f700a += self.text + '#'
            elif self.key == 'c' and self.text != '':
                self.f700c += self.text + '#'
            elif self.key == 'd' and self.text != '':
                self.f700d += self.text + '#'                                
        elif self.parent == '710':
            if self.key == 'a' and self.text != '':
                self.f710a += self.text + '#'
        elif self.parent == '720':
            if self.key == 'a' and self.text != '':
                self.f720a += self.text + '#'                
        elif self.parent == '776' :
            if self.key == 'i':
                self.f776i = self.text
            elif self.key == 'z':
                self.f776z = self.text
        elif self.parent == '830':
            if self.key == 'a':
                self.f830a = self.text
            
    def characters(self, content):
        #print(self.parent + " " + self.key + " " + content)
        self.text = content.strip()
        

    ##Write data to CSV file
    def csvWriter(self, fileName):
        global rowsList
        
        df = pd.DataFrame(rowsList, columns = ['f001', 'f020a', 'f040b', 'f100a', 'f100e', 
                         'f245a', 'f245b', 'f245c', 'f245n', 'f245p', 
                         'f246a', 'f263a', 'f264a', 'f264b', 'f264c', 
                         'f300a', 'f300b', 'f300c', 'f336a', 'f338a', 'f347a', 
                         'f347b', 'f490a', 'f504a', 'f500a', 'f588a',
                         'f600a', 'f600d', 'f6001',
                         'f651a', 'f651x', 'f650a', 'f650x', 'f650z', 
                         'f700a', 'f700c', 'f700d', 'f710a', 'f720a', 
                         'f776i', 'f776z', 'f830a'])
        
        df.to_csv(fileName, sep='\t', compression='gzip')
    	
    	    
parser = xml.sax.make_parser()
handler = MARC_Handler()
parser.setContentHandler(handler)
parser.parse('test.xml')
parser.parse('../data/nls-nbs-v2/NBS_v2_validated_marcxml.xml')
#handler.csvWriter('../data/output/test.csv.gz')
handler.csvWriter('../data/output/nbs.csv.gz')

    