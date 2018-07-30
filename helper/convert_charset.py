from bs4 import BeautifulSoup

def convert(file, coding):
    f = open(file)
    
    
    
f = open("schiller.txt")
soup = BeautifulSoup(f.read(),"html5lib" )
g = soup.get_text().encode('ISO-8859-2')
