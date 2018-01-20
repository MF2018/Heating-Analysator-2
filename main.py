# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:32:16 2018

@author: Dela
"""
"""
This main function uses pyxlsDownloader to search for Download-elements of a homepage. 
Then it downloads the link in a second step.
In a third step it uses the Analyser to analyse the Data and plot a part of the data.
In a third step the Analyser uploads the Data to Google Drive using an API client. The google upload bases on the module of
google_drive_util.py on github:https://gist.github.com/lheric/876a924c5d77bde0f62526c7fa6ad846 .
To use the API client the users has to generate 'client_secrets.json' from https://console.developers.google.com/ . 

The code of the main function is only rudimental. In further step a gui will be provided. 
So, the user can enter a homepage of his wish and can choose more then one download link.
After that he can choose the columns for the data-analysis and which data he wants to plot.
But this will be in a further step
"""
from CSV_download import pyxlsDownloader 
import os
import sys
from analyser import analyser





def main(argv):
    
    #main-routine
    #initialisation of the Downloader 
    Downloader= pyxlsDownloader()
    
    #initialisation of the Analyser
    Analyser = analyser()

    #building a file name
    #path of the current project
    directory = os.getcwd()
    #path for the output-folder
    path = directory + "\load_profils"
    #initialisation of the name of the output file
    name = ""
    
    #get the download links from a homepage;In a further step the link can be set in a gui
    links,count,error = Downloader._getFilesFromPage('https://www.ednetze.de/kunde/lieferanten/lastprofile-temperaturtabellen/')
    
    # print the links for the user
    print 'Choose the link of your choice'
    for i in links:
        print i
    print
    
    #the user can chooses a link for the next steps 
    #in a further step the user can select more than one link(checkboxes)
    x = raw_input('Select a number  :')
    
    #up to now, there is no loop until the user decides to leaf. This will be provided with a gui in a further step.
    
    
    
    # checking if the input is of the wrong datatype
    page = ()
    try:
        x = int(x)
    
        if x<1 or x>= count:
           print 'Wrong number. Please try a different one.'
           error = 1
        else:
             #select download link
           page = links[x-1][1] 
    except:
        print 'Wrong type'
        error ==1
        

     
    #call of the file-downloader, if no error happens before.
    if error == 0:
       returnvalue,error = Downloader._Downloader(page,path,name)

       #handling of the returned file
       if error==1:
       #error handling
          print "It is not possible to load the file."
       elif error == 2:
          print "Can't reach the homepage"
       elif error == 3:
          print "No useable data" 
    
    if error==0:
        #read the sheets name    
        sheets,error = Analyser._getSheet(returnvalue)
        
        
        
        #handling of the returned sheets
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
    
           #the user can chooses a sheet for the next steps 
           x = raw_input('Select a number  :')  
           try:
              x = int(x)
    
              if x<1 or x> index:
                 print 'Wrong number. Please try a different one.'
                 error = 1
              else:
                 #read the file and transfer the data to a data frame 
                 input_data,error = Analyser._read(returnvalue,sheets[x-1])
          
           except:
              print 'Wrong type'
              error ==1
              
        else:
            #if the file is a csv-file it has no sheets
            #read the file and transfer the data to a data frame
            input_data,error = Analyser._read(returnvalue,'')
            
        
        #analysation of the data and upload data to google 
        if error ==0:
           x = raw_input( 'Insert filename: ')
           col =2
           error = Analyser._analyse(input_data,x,col)
           if error ==1:
              print "Analysation failed"
           elif error ==2:
               print "failed to upload file"
                
        
   
if __name__ == "__main__":
    main(sys.argv)