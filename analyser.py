# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:48:54 2018

@author: Max
"""
"""This class analyses an excel-file.
It has noch eingaben methods:
1) read_file reads an excel-file 
2) analyse analyses the document and plots the data

It has one global variable error which reinitialyses at every call with 0 
Every errorvalue except 0 means an error
"""

import pandas as pd
from pathlib import Path
from google_uploader import Google_login
import numpy as np
import scipy.stats as stats
import pylab as pl

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
       
    
   #function to save an Excel file 
   #  a filename and the data is transfered to the function
   #  it returns an error type
   def _saveExcel(self,name,data):
       
       #try:
          writer = pd.ExcelWriter(name+'.xls', engine='xlsxwriter')

          # Convert the dataframe to an XlsxWriter Excel object.
          data.to_excel(writer,sheet_name='Sheet')

          
       #except:
        #  self.error=1
          
          return writer,self.error
       
   #function to save an Excel file 
   #  an excel image and the sheet name is transfered to the function
   #  it returns an error type
   def _addSheet(self,writer,data,sheet):
       
       try:

          # Convert the dataframe to an XlsxWriter Excel object.
          data.to_excel(writer, sheet_name=sheet)

          
         
       except:
          self.error=1
          
       return writer,self.error

   #function to analyse the date. It calls supfunction for that
   #  a data-file
   #  it returns an error type
   def _analyse(self,input_data,filename,col):
       try:
          #test werte
          input_data = input_data.convert_objects(convert_numeric=True)
        
          ###pandas 17 does not work. Upgrade failed. So it will be done later
          """ b,error = Analyser._removeOutliners(a)"""
         
          statistic_data = input_data.describe()
       
     
          # Create a Pandas Excel writer using XlsxWriter as the engine.
          # It is possbible that the asci transformation of xlswriterfails
          # So a asci transformation will be added in a further step    
          writer,error = self._saveExcel(filename,input_data)
          writer,error = self._addSheet(writer,statistic_data,'1')
          error = self._plotData(input_data,col,writer)
          writer.save()
          self.error = error
          if error ==0:
             error = self.googleupload(filename) 
             self.error = error
         
       except:
          self.error=1
         
       return self.error       
       

   #function a plot to an 
   #  the data-file and the column to plot is transfered to the function
   #  it returns an error type
   def _plotData(self,data,col,writer):
       try:
          data[col].plot()
          #In a further step the plot shall be saved in the xls-file
          
          # Access the XlsxWriter workbook and worksheet objects from the dataframe.
          workbook  = writer.book
          worksheet = writer.sheets['Sheet']             
           
          # Create a chart object.
          chart = workbook.add_chart({'type': 'line'})
          
          chart.add_series({
            'values':     ['Sheet',1,col,data.shape[0] ,col],
             })
          
          # Insert the chart into the worksheet.
          worksheet.insert_chart('G2', chart)
          
       except:
          self.error=1
          
       return self.error       
    
   #function to upload all xls files in this folder
   # the file_name is transfered to the function
   def googleupload(self,file_name):
       try:
          Uploader = Google_login() 
          new_folder = Uploader.create_subfolder(None,file_name)
          Uploader.upload_files_to_folder(Uploader.list_files_with_ext('.xls')[:3],new_folder)
       except:
           self.errror = 2
       return self.error