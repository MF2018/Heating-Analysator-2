# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:32:16 2018

@author: Dela
"""
"""
This main function uses pyxlsDownloader to search furst for Download-elements at an homepage. 
Then it downloads the link in a second step.
In a third step it uses the statisticAnalyser to analyse the Data and plot it. 
"""
from CSV_download import pyxlsDownloader 
import os
import sys
from analyser import analyser
import pandas as pd



def main(argv):
    
    #main- routine
  
    #initialisation of the Downloader 
    Downloader= pyxlsDownloader()
    
    #initialisation of the Analyser
    Analyser = analyser()

    #building a file name
    #path of the current project
    directory = os.getcwd()
    #path for the output-folder
    path = directory + "\load_profils"
    #name of the output file
    #when the gui is finished, it is possible to define the name
    name = ""
    
    #get the download links from an homepage
    links,count,error = Downloader._getFilesFromPage('https://www.ednetze.de/kunde/lieferanten/lastprofile-temperaturtabellen/')
    
    # print the links for the user
    print 'Choose the link of your choice'
    for i in links:
        print i
    print
    
    #the user can choooses a link for the next steps 
    x = raw_input('Select a number  :')
    
    #loop um eingabe fehlt noch
    
    
    
    # checking if the input a wrong datatype
    try:
        x = int(x)
    
        if x<1 or x>= count:
           print 'Ungültige Eingabe, bitte geben Sie eine andere Zahl ein'
           error = 1
        else:
             #link of the homepage wich provides the data
           page = links[x-1][1] 
    except:
        print 'Wrong type'
        error ==1
        

     
    #call of the file Downloader  if no error happens before
    if error == 0:
       returnvalue,error = Downloader._Downloader(page,path,name)

       #handling of the returned values
       if error==1:
       #error handling
          print "It is not possible to load the file."
       elif error == 2:
          print "Can't reach the homepage"
       elif error == 3:
          print "No useable data" 
    
     #if succesfull print filename
    if error==0:
        #read the sheets name
    
        #input_data,error = Analyser._read(returnvalue)      
        sheets,error = Analyser._getSheet(returnvalue)
        print sheets 
        
        
        
        #handling of the returned values
        if error==1:
        #error handling
           print "Can't read file."
           
        elif sheets != ():
           # chosse the sheet 
           # print the links for the user
           print 'Choose the link of your choice'
           for index,sheet in enumerate(sheets,start =1):
              print '-'+str(index)+'- ' + sheet
           print
    
           #the user can choooses a sheet for the next steps 
           x = raw_input('Select a number  :')  
           try:
              x = int(x)
    
              if x<1 or x> index:
                 print 'Ungültige Eingabe, bitte geben Sie eine andere Zahl ein'
                 error = 1
              else:
                 input_data,error = Analyser._read(returnvalue,sheets[x-1])
          
           except:
              print 'Wrong type'
              error ==1
              
        else:
            input_data,error = Analyser._read(returnvalue,'')
            
        #test werte
        print input_data
        a = input_data.describe()
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        a.to_excel(writer, sheet_name='Sheet1')

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
           
            
   
if __name__ == "__main__":
    main(sys.argv)