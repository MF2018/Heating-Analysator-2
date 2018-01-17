# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:32:16 2018

@author: Dela
"""

from CSV_download import pyxlsDownloader 
import os
import sys
import urllib2
from bs4 import BeautifulSoup 

def main(argv):
    
    #main- routine
  
    #initialisation of object used
    Downloader= pyxlsDownloader()


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
    print 'Choose the link of your choice'
    for i in links:
        print i
    print
    
    #chose a link for the next steps 
    x = raw_input('Select a number  :')
    
    #loop um eingabe fehlt noch
    
    
    
    # checking if it's a wrong datatype
    try:
        x = int(x)
    
        if x<1 or x>= count:
           print 'Ungültige Eingabe, bitte geben Sie eine andere Zahl ein'
        else:
           print links[x-1][1] 
    except:
        print 'Wrong type'
        
        
    #link of the homepage wich provides the data
    page = "https://www.ednetze.de/fileadmin/ednetze/Excel/Kunde/Lieferanten/Lastprofile/VDEW-Lastprofile-Haushalt.xls"   
    #call of the xls-function  

    returnvalues,error = Downloader._Downloader(page,full_filename)

    #handling of the returned values
    if error==1:
       #error handling
       print "It is not possible to load the file."
    else:
       #if succesfull print filename
       print returnvalues
   
   
if __name__ == "__main__":
    main(sys.argv)