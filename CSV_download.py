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
import urllib2
import os
import urlparse
from posixpath import basename
from bs4 import BeautifulSoup 



#Global class for the xls-Downlader

class pyxlsDownloader(object):
        
    #init function with class constants as constructor
   def __init__(self):
      #initialising error-variable with default value
      self.error = 0
      
   #function to download a csv-file
   #  an url and a filename are transfered to the function
   #  it returns the filename including the path for further file-analysations and an error type
   def _Downloader(self,url,path,name):
    
      
      #if no filename is transfered, the filename of the url is used
      if name =='':
         #decompsing url for filename
         decomposed_url = urlparse.urlparse(url) 
         #extractin filename
         filename =  basename(decomposed_url.path)
         #replace _, because urlretriever doesn't work with _
         filename = filename.replace('_','')
         #creating a full filename including path to use subfolders
         full_filename = os.path.join(path,filename)
      else:
         #replace _, because urlretriever doesn't work with _
         name = full_filename.replace('_','') 
          #creating a full filename including path to use subfolders
         full_filename = os.path.join(path,name)
         
      #file extraction   
      #exception if the transfer doesn't work
      #the handling of the error type is in the main routine
      try:
         #download file
         urllib.urlretrieve(url,full_filename)
         
      except:
         self.error = 1
      
      #returning filenmame for further processing
      return full_filename,self.error
      
      
   #function to extracts download links from homepag
   #  an url is transfered to the function and it scrapes a page for download-elements
   #  if there are download elements it extract the link 
   # it returns the links for a filedownload and the error value and the element number   
   def _getFilesFromPage(self,url):
      downloadLink =[]
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
            downloadLink.append([str(index),parse_object.scheme+'://'+
                parse_object.netloc+link['href']]) 
            
         if index == 0:
            #no data error 
            self.error = 3 
      except:
         self.error = 2 
      return downloadLink,index, self.error