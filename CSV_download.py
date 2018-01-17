# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:19:00 2018

@author: Max
"""
"""This project helps to collect customer load profils of heating sytems in Germany and analyses it."""

import urllib
import time
import urllib2
import urlparse
from bs4 import BeautifulSoup 



#Global class for the xls-Downlader

class pyxlsDownloader(object):
        
    #init function with class constants as constructor
   def __init__(self):
       #class constants
      self.datatype = ".xls"
      #initialising error-variable with default value
      self.error = 0
      
   #function to download a csv-file
   #  an url and a filename are transfered to the function and the function adds a timestamp 
   def _Downloader(self,url,name):
    
      #timestamp to avoid data conflicts
      timestamp = time.strftime("%Y_%m_%d_%H_%M_%S",time.gmtime())
      filename = name + "_" + timestamp + self.datatype

      #file extraction   
      #exception if the transfer doesn't work
      #the handling of the error type is in the main routine
      try:
         urllib.urlretrieve(url,filename)
         
      except:
         self.error = 1
      
      #returning filenmame for further processing
      return filename,self.error
      
      
   #extracts download links from homepage   
   def _getFilesFromPage(self,url):
      list =[]
      try:
          #crations a conection to a hompage
         html= urllib2.urlopen(url)   
         #extracts the html code of a page
         soup = BeautifulSoup(html.read().decode("iso-8859-1"))
         load_profil = soup.find_all('a', attrs={'class', 'download'})
         
         #decompsoing link to geht the adress for the download link
         parse_object = urlparse.urlparse(url)
         #creatoing a list element with all download links
         x = 1;
         for i in load_profil: 
            #creating an url entry 
            list.append(['-'+str(x)+'-',parse_object.scheme+'://'+
                parse_object.netloc+i['href']]) 
            x = x+1
            
         if x == 0:
            #no data error 
            self.error = 3 
      except:
         self.error = 2 
      return list,x, self.error