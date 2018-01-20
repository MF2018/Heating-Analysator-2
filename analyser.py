# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:48:54 2018

@author: Max
"""
"""This class analyses an excel-file.
It has 7 methods:
1) read reads an excel-file. 
2) getSheets selects one sheet of an excel file.
3) saveExcel writes the analysed data in an excel file.
4) addSheet adds a sheet to an existing excel file.
5) analyse analyses the document, plots the data, save it and uploads the file to google drive.
6) plotDate plots a selected Data column and adds it to excel. In a further step a nominal 
   distribution will be added.
7) googleupload uploads the document to google drive.

It has one global variable error which reinitializes at every call with 0 
Every error value except 0 means an error.
"""

import pandas as pd
from pathlib import Path
from google_uploader import Google_login


#Global class for the analyser

class analyser(object):
        
    #init function with class constants
   def __init__(self):
      #initialising error-variable with default value
      self.error = 0
      
      
   #function to read an excel-file
   #  a filename including the path and the excel sheet is transferred to the function
   #  it returns a data array and an error type
   def _read(self,filename,sheet):
      
      #decomposing the filename to get the right reader
      try:
         #get the suffix of the file 
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
   #  a filename including the path is transferred to the function
   #  it returns the sheets of an excel-file and an error type   
   def _getSheet(self,files):
       sheets =()
       try:
          #reading the sheetsname if they are an xls file
          
          if 'xls' in Path(files).suffix: 
             sheet = pd.ExcelFile(files) 
             sheets = sheet.sheet_names
             print sheets
       except:
          self.error = 1
              
       return sheets,self.error
       
    
   #function to save an excel file 
   #  a filename and the data are transferred to the function
   #  it returns an error type
   def _saveExcel(self,name,data):
       
       try:
          writer = pd.ExcelWriter(name+'.xls', engine='xlsxwriter')

          # Converts the data frame to a XlsxWriter object.
          data.to_excel(writer,sheet_name='Sheet')

          
       except:
          self.error=1
          
       return writer,self.error
       
   #function to add an excel sheet 
   #  an excel image and the sheet name is transferred to the function
   #  it returns an error type
   def _addSheet(self,writer,data,sheet):
       
       try:

          # Converts the data frame to an XlsxWriter object.
          data.to_excel(writer, sheet_name=sheet)

          
         
       except:
          self.error=1
          
       return writer,self.error

   #function to analyse the date. It calls sup functions for that
   #  a data-file, a filename and a value for a column is transferred to the function
   #  it returns an error type

   def _analyse(self,input_data,filename,col):
       try:
          #convertsvalues to a numeric value
          input_data = input_data.convert_objects(convert_numeric=True)
        
          #it was not possible to upgrade to pandas 0.17.0. 
          #So, the outliners and not numeric values are removed in a further step of programming          
          # input_data,error = Analyser._removeOutliners(input_data)
         
          #statistic evaluation of the data
          statistic_data = input_data.describe()
       
     
          # It is possible  that the asci transformation of xlswriterfails
          # An asci transformation will be added in a further step.
     
          # Creates an Excel writer using XlsxWriter as the engine.
          writer,error = self._saveExcel(filename,input_data)
          writer,error = self._addSheet(writer,statistic_data,'1')
          error = self._plotData(input_data,col,writer)
          #writes the excel document
          writer.save()
          self.error = error
          if error ==0:
             #uploads the excel document 
             error = self.googleupload(filename) 
             self.error = error
         
       except:
          self.error=1
         
       return self.error       
       

   #function to plot a data column 
   #  the data file and the column to plot and a writer image to save it to excel 
   # is transferred to the function.
   #  it returns an error type.
   def _plotData(self,data,col,writer):
       try:
          data[col].plot()
          #In a further step a nominal distribution will be added, too.
          
          # Access the XlsxWriter workbook and worksheet objects from the data frame.
          workbook  = writer.book
          worksheet = writer.sheets['Sheet']             
           
          # Creates a chart object.
          chart = workbook.add_chart({'type': 'line'})
          
          #Adds a data series to the chart
          chart.add_series({
            'values':     ['Sheet',1,col,data.shape[0] ,col],
             })
          
          # Insert the chart into the worksheet.
          worksheet.insert_chart('G2', chart)
          
       except:
          self.error=1
          
       return self.error       
    
   #function to upload all xls files in this folder to google drive
   # the file_name is transferred to the function.
   #  it returns an error type.
   def googleupload(self,file_name):
       try:
          #creating an authorized google access            
          Uploader = Google_login() 
          #add new folder to google drive
          new_folder = Uploader.create_subfolder(None,file_name)
          #uploads all xls files of the working directory
          Uploader.upload_files_to_folder(Uploader.list_files_with_ext('.xls')[:3],new_folder)
       except:
           self.errror = 2
       return self.error