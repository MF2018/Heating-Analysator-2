# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:19:00 2018

@author: Max
"""
"""This class looks for downloadable elements on a page and downloads it.
It has two methods:
1) getFilefromPage scrapes a page for download elements 
2) Downloader downloads the element

It has one global variable error which reinitializes at every call with 0. 
Every error value except 0 means an error
"""

import urllib
import urllib2
import os
import urlparse
from posixpath import basename
from bs4 import BeautifulSoup 



#Global class for the xls-Downloader

class downloader(object):
        
    #init function with class constants
   def __init__(self):
      #initializing error-variable with default value
      self.error = 0
      
   #function to download a file
   #  an url and a filename are transferred to the function
   #  it returns the filename including the path for further file-analysations and an error type
   def _downloadFiles(self,url,path,name):
    
      
      #if no filename is transferred, the filename of the url is used
      if name =='':
         #decompsing url for filename
         decomposed_url = urlparse.urlparse(url) 
         #extracting filename
         filename =  basename(decomposed_url.path)
         #replace '_' , because urlretriever doesn't work with _
         filename = filename.replace('_','')
         #creating a full filename including the path to use subfolders
         full_filename = os.path.join(path,filename)
      else:
         #replace _, because urlretriever doesn't work with _
         filename = name.replace('_','') 
          #creating a full filename including the path to use subfolders
         full_filename = os.path.join(path,filename)
         
       
      #exception if the transfer doesn't work
      #the handling of the error type is in the main routine
      try:
         #download file
         urllib.urlretrieve(url,full_filename)
         
      except:
         self.error = 1
      
      #returning filenmame for further processing
      return full_filename,self.error
      
      
   #function to extract the download links from a homepage
   #  an url is transferred to the function and it scrapes the page for download-elements
   #  if there are download elements it extracts the links 
   # it returns the links for a file download and the error value and the numbers of elements  
   def _getFilesFromPage(self,url):
      downloadLink =[]
      try:
          #creation of a connection to a homepage
         html= urllib2.urlopen(url)   
         #extracts the html code of a page
         soup = BeautifulSoup(html.read().decode("iso-8859-1"))
         load_profil = soup.find_all('a', attrs={'class', 'download'})
         
         #decomposing the link to get the address for the download link
         parse_object = urlparse.urlparse(url)
         #creating a list element with all download links
         for index,link in enumerate(load_profil,start =1): 
            #creating an url for the download
            downloadLink.append([str(index),parse_object.scheme+'://'+
                parse_object.netloc+link['href']]) 
            
         if index == 0:
            #no data error 
            self.error = 3 
      except:
         self.error = 2 
      return downloadLink,index, self.error