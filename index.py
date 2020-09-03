import requests
from bs4 import BeautifulSoup
import re
import json 
import csv
#webswite url
urls=''


#loda data from website
with open ('website.txt','r') as f:
    for line in f.read():
        urls+=line

urls=list(filter(None,urls.split('\n')))        


#extract data
#loop
for url in urls:
    res=requests.get(url)
    print('crawl base url:',res.url)
    #pars responce
    content=BeautifulSoup(res.text,'lxml')
#     extarct contact
    try:
        contact=content.find('a',text=re.compile('contact',re.IGNORECASE))['href']
        if 'http' in contact:
            contact_url=contact
        else:
            contact_url=res.url[0:-1]+contact
        res_contact=requests.get(contact_url)
        contact_content=BeautifulSoup(res_contact.text,'lxml').get_text()
        print(contact_content)
        res_contact=requests.get(contact_url)
        print("crawl contact Url:",res_contact.url)
        emails=re.findall('(\w+@\w+.\w+\.\w+)', contact_content )
        phones=re.findall('(\d{3,4}\d{3,4}\d{3,4})', contact_content )
        print('\nEMAILS:',emails)    
        print('\nPHONE:',phones) 
    except  :
         pass