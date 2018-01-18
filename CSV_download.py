# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:19:00 2018

@author: Max
"""
"""This class looks for downloadable elements on a page and downloads it.
It has two methods:
1) getFilefromPage srapes a page for download elements 
2) Dowloader downloads the element

It has one global variable error which reinitialyses at every call with 0 
Every errorvalue except 0 means an error
"""

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
   #  an url and a filename are transfered to the function and the function adds a timestamp and saves the file
   #  it returns the filename including the path for further file-analysations and an error type
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
      
      
   #function to extracts download links from homepag
   #  an url is transfered to the function and it scrapes a page for download-elements
   #  if there are download elements it extract the link 
   # it returns the links for a filedownload and the error value and the element number   
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
         for index,link in enumerate(load_profil,start =1): 
            #creating an url entry 
            list.append([str(index),parse_object.scheme+'://'+
                parse_object.netloc+link['href']]) 
            
         if index == 0:
            #no data error 
            self.error = 3 
      except:
         self.error = 2 
      return list,index, self.error