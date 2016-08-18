# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:37:53 2015

@author: Sapna
"""

import urllib2,re,sys

#make a new browser, this will download pages from the web for us. This is done by calling the 
#build_opener() method from the urllib2 library
browser=urllib2.build_opener()

#desguise the browser, so that websites think it is an actual browser running on a computer
browser.addheaders=[('User-agent', 'Mozilla/5.0')]


#number of pages you want to retrieve (remember: 10 freelancers per page)
pagesToGet=100
pageIndex=0

#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
fileWriter=open('jobPages.txt','w')

#for every number in the range from 1 to pageNum+1  
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page

    #url='http://www.indeed.com/jobs?as_and=&as_phr=data+scientist&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=United+States&fromage=any&limit=10&sort=&psf=advsrch'
    url='http://www.indeed.com/jobs?q=%22data+scientist%22&l=United+States&radius=0&start='+str(pageIndex)

    try:
        #use the browser to get the url.
        response=browser.open(url)    
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()

    unique=set()#remember unique names	

    jobLinkType1=re.findall('class="jobtitle turnstileLink" href="?\'?([^"\'>]*)',myHTML)#get all the matches for those links that open in Indeed website
    jobLinkType2=re.findall('rel="nofollow"\nhref="?\'?([^"\'>]*)',myHTML)#get all the matches for those jobs that open in an external website
    
    for jobType1 in jobLinkType1:
        unique.add(jobType1)
        
    for jobType2 in jobLinkType2:
        unique.add(jobType2)

    #write the results
    for jobname in unique:
        fileWriter.write('http://indeed.com/'+jobname+'\n')
    pageIndex +=10

#close the file. File that are opened must always be closed to make sure everything is actually written and finalized.
fileWriter.close()
