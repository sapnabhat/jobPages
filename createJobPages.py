# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:12:26 2015

@author: Sapna
"""

# import the libraries we will be using
import urllib2,os,sys,time

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

jobNumber = 1
# this is the name of the folder where we will download the job pages.
outFolder='JobPages'

# if the folder doesn't exist, make it 
if not os.path.exists(outFolder): # use path.exists() from the os library to check if something exists
    os.mkdir(outFolder) # use mkdir() from the os library to make a new directory

# open a connection to the file you want to read
fileReader=open('jobPages.txt')
for line in fileReader: # this syntax allows us to read the file line-by-line
        
        link=line.strip() # .strip() removes white spaves and line-change characters from the beginning and end of a string
        
        print 'Donwloading: ', link
        
        try:
            #use the browser to get the url.
            response=browser.open(link)  
            time.sleep(2)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',link
            print error_type, 'Line:', error_info.tb_lineno
            continue
    
        html=response.read()   
        #time.sleep(2)
        pageName= 'DataScientistJob'+str(jobNumber)
        
        #open a new file in the pre-specified folder, write the html  , and close it.
        fileWriter=open(outFolder+'/'+pageName+'.html', 'w')
        fileWriter.write(html)
        fileWriter.close()
        jobNumber+= 1
   
fileReader.close()