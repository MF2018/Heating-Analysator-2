# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 09:55:10 2018

@author: Max
"""
"""This class uploads a file to google and uses its api. It bases on the model 
 google_drive_util.py on github:https://gist.github.com/lheric/876a924c5d77bde0f62526c7fa6ad846

It has one global variable error which reinitialyses at every call with 0 
Every errorvalue except 0 means an error
"""

#Global class for the xls-Downlader


## Simple Python module to upload files to Google Drive
# Needs a file 'client_secrets.json' in the directory 
# The file can be obtained from https://console.developers.google.com/ 
# under APIs&Auth/Credentials/Create Client ID for native application

# To test usage:
# import google_drive_util
# google_drive_util.login()
# google_drive_util.test()


import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Google_login(object):
        
   #init function with class constants as constructor
   def __init__(self):
      #initialising error-variable with default value
      global gauth, drive
      gauth = GoogleAuth()
      gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication
      drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance
      self.error = 0
      
      
   def root_files(self):    
      file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
      # Auto-iterate through all files in the root folder.
      #for file1 in file_list:
      #    print 'title: %s, id: %s' % (file1['title'], file1['id'])
      return file_list


   def find_folders(self,fldname):
       file_list = drive.ListFile({
           'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
           }).GetList()
       return file_list


   def create_subfolder(self,folder,sfldname):
       new_folder = drive.CreateFile({'title':'{}'.format(sfldname),       
                              'mimeType':'application/vnd.google-apps.folder'})
       if folder is not None:
          new_folder['parents'] = [{u'id': folder['id']}]
       new_folder.Upload()
       return new_folder


   def list_files_with_ext(self,ext,dir='./'):
       return sorted(filter(lambda f:f[-len(ext):]==ext,os.listdir(dir)))


   def upload_files_to_folder(self,fnames, folder):
       for fname in fnames: 
           nfile = drive.CreateFile({'title':os.path.basename(fname),
                                 'parents':[{u'id': folder['id']}]})
           nfile.SetContentFile(fname)
           nfile.Upload() 







