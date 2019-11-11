#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:27:51 2019

@author: brianmarx
"""

class RISParser(object):
                    
    idDict = {}
    
    tags = ['TY','A1','A2','A3','A4','AB','AD','AN','AU','AV',
'BT','C1','C2','C3','C4','C5','C6','C7','C8','CA','CN','CP',
'CT','CY','DA','DB','DO','DP','ED','EP','ET','ID','IS','J1',
'J2','JA','JF','JO','KW','L1','L2','L3','L4','LA','LB','LK',
'M1','M2','M3','N1','N2','NV','OP','PB','PP','PY','RI','RN',
'RP','SE','SN','SP','ST','T1','T2','T3','TA','TI','TT','U1',
'U2','U3','U4','U5','UR','VL','VO','Y1','Y2','ER']

    def __init__(self):
        pass
    
    def __init_(sIn, array):
        s = sIn
        arr = array
# 
#    def findTag(self, tag): 
#        if tag in self.tags:
#            print('Found tag: ' + tag)

    #finds the different ids in each record and counts each occurance
    def idOperation(self, idStr):
        newStr = idStr.split(';')
        newStr = [x.lstrip().rstrip() for x in newStr]
        
        for s in newStr:
            if not s in self.idDict: 
                self.idDict[s] = 1
            else:
                self.idDict[s] = self.idDict[s] + 1
    
    def getIDs(self, content):
        for line in content:
            if line[0:2] == 'ID':
                    self.idOperation(line[3:])
             
    # Returns an array of dictionaries
    # Each dictionary is a record broken up by
    # the tag.   ID TI SO PB PD
    def getRecords(self, content):
        records = []
        record = {}
        temp = ''
        for line in content:
            
            if not line[0:2] == 'ER':
                if line[0:2] == '  ':
                    newrec = record[temp] + ' ' + line.lstrip()
                    record[temp] = newrec
                else :
                    temp = line[0:2]
                    record[temp] = line[3:]
                    
            else:
                records.append(record)
                record = {}
        return records
        
    def processFile(self, content, tags):
        
        records = self.getRecords(content)
        for r in records:
            for tag in tags:
                if tag in self.tags and tag in r.keys():
                    print(tag)
                    print(r[tag])

    def printDict(self):
        print(self.idDict)
        
    def clearDict(self):
        self.idDict.clear()