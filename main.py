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

def main(argv):
    
    #main- routine
  
    #initialisation of the Downloader 
    Downloader= pyxlsDownloader()


    #building a file name
    #path of the current project
    directory = os.getcwd()
    #path for the output-folder
    path = directory + "\load_profils"
    #name of the output file
    name = "load_profil"

    #full filename including path to use subfolders
    full_filename = os.path.join(path,name)
    
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
        else:
             #link of the homepage wich provides the data
           page = links[x-1][1] 
    except:
        print 'Wrong type'
        
    
     
    #call of the file Downloader  if no error happens before
    if error == 0:
       returnvalues,error = Downloader._Downloader(page,full_filename)

    #handling of the returned values
    if error==1:
       #error handling
       print "It is not possible to load the file."
    elif error == 2:
       print "CanÄ't reach the homepage"
    elif error == 3:
       print "No useable data" 
    else:
       #if succesfull print filename
       print returnvalues
   
   
if __name__ == "__main__":
    main(sys.argv)