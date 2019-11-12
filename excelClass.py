#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:11:35 2019

@author: brianmarx
"""

from openpyxl import Workbook

class excelClass(object):
    
    def __init__(self):
        pass
    
    wb = Workbook()
    
    def makeWorkbook(self, inputDict, title, saveTitle):
        self.wb.title = title
        ws = self.wb.active
        ws.title = 'Data'
        self.wb.save(saveTitle + '.xlsx')