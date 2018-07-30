# Import all the necessary libraries

import os
import sys

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# Unter dem folgenden Link (base) finden sich alle Gedichte von Friedrich Schiller auf gutenberg.spiegel.de
# die einzelnen Ausgaben werden dahinter einfach hochgezählt (max 154)
# mit folgendem Script könnten die Gedichte heruntergeladen und in eine Textdatei abgespeichert werden.
# 


base = 'http://gutenberg.spiegel.de/buch/gedichte-9097/'

for n in range(41, 156):
    print(n)
    url = base + str(n)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req)
    content = url.read()
    soup = BeautifulSoup(content, 'lxml')
    
    text = ''
    
    div = soup.findAll("div",{"id" : "gutenb"})
    for tag in div:
        t = tag.get_text()
        text += t

    tempfile = 'temp.txt'
        
    with open(tempfile, 'w') as temp:
        temp.write(text)

    # open the textfile
    with open(tempfile, 'r') as f:
        text_lines = f.readlines()
        f.close()
    
    # get the title of the poem
    title = text_lines[1]
    
    # folgendes ist notwendig, damit der new line character nicht im 
    # titel erscheint. 
    title = title[:-2]
    print(title)
    #write the poem into its own textfile
    with open('./input/txt/to_process/' + str(title) + '.txt', 'w') as pfile:
        pfile.write(text)
        

    ## Try to delete the temp file ##
    try:
        os.remove(tempfile)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))
   
 

