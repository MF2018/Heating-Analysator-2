# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:48:54 2018

@author: Max
"""
"""This class analyses an excel-file.
It has two methods:
1) read_file reads an excel-file 
2) analyse analyses the document and plots the data

It has one global variable error which reinitialyses at every call with 0 
Every errorvalue except 0 means an error
"""

import pandas as pd
from pathlib import Path
import numpy as np

#Global class for the analyser

class analyser(object):
        
    #init function with class constants as constructor
   def __init__(self):
      #initialising error-variable with default value
      self.error = 0
      
      
   #function to read an excel-file
   #  a filename including the path and the excelsheet is transfered to the function
   #  it returns an data array, an error type
   def _read(self,filename,sheet):
      
      #decomposing the filename to get the right reader
      try:
         #get the suffixof the file 
         extension = Path(filename).suffix
         
         #reading a xls document
         if 'xls' in extension:
            data = pd.read_excel(filename,sheet,header=None)
        
         #reading a csv document
         elif 'csv' in extension:
            data = pd.read_csv(filename,sep=';',header=None)
             
      except:
         self.error = 1  
      return data,self.error
         
         
   #function to get the sheets of an excel-file
   #  a filename including the path is transfered to the function
   #  it returns the sheets of an excel-fiele and an error type   
   def _getSheet(self,files):
       sheets =()
       try:
          #reading the sheetsname 
          
          if 'xls' in Path(files).suffix: 
             sheet = pd.ExcelFile(files) 
             sheets = sheet.sheet_names
             print sheets
       except:
          self.error = 1
              
       return sheets,self.error
       
   #function to remove outliners an Excel file 
   #  a filename and the data is transfered to the function
   #  it returns a new data file without outliners and an error type
   def _removeOutliners(self,data):
       #try:
          
          mean = data.mean()
          difference = data-mean
          #keep only the ones that are within +3 to -3 standard deviations in the column 'Data'.
          data = [(abso <3).all(axis=1)]
          
       #except:
        #  self.error=1
          
          return data,self.error
       
    
   #function to save an Excel file 
   #  a filename and the data is transfered to the function
   #  it returns an error type
   def _saveExcel(self,name,data):
       
       #try:
          writer = pd.ExcelWriter(name+'.xls', engine='xlsxwriter')

          # Convert the dataframe to an XlsxWriter Excel object.
          data.to_excel(writer, sheet_name='Sheet')

          # Close the Pandas Excel writer and output the Excel file.
          writer.save()
       #except:
        #  self.error=1
          
          return self.error
       
   #function to save an Excel file 
   #  a filename and the data and the sheet name is transfered to the function
   #  it returns an error type
   def _addSheet(self,name,data,sheet):
       
       try:
          writer = pd.ExcelWriter(name+'.xls', engine='xlsxwriter')

          # Convert the dataframe to an XlsxWriter Excel object.
          data.to_excel(writer, sheet_name=sheet)

          # Close the Pandas Excel writer and output the Excel file.
          writer.save()
       except:
          self.error=1
          
       return self.error
       