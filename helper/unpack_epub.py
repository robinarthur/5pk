from bs4 import BeautifulSoup
import zipfile
import os.path
import glob
from chardet.universaldetector import UniversalDetector

def unzip(source_filename, dest_dir):
    """this function unzips all the files from the epub file
        the following functions should only need the textfiles"""
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                while True:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if not drive:
                        print("no drive")
                        break
                if word in (os.curdir, os.pardir, ''):
                    continue
                path = os.path.join(path, word)
            zf.extract(member, path)

def load_txt(dir):
    for path in glob.glob(dir + '/*.html'):
        with open(path) as markup:
            soup = BeautifulSoup(markup.read(),"html5lib" )
        with open("strip_" + path, "w") as f:
            f.write(soup.get_text().encode('ISO-8859-2'))

def detect(file):
    detector = UniversalDetector()
    for filename in glob.glob(file):
        print(filename.ljust(60),detector.reset())
        for line in file(filename, 'rb'):
            detector.feed(line)
            if detector.done:
                break
    
    detector.close()
    print(detector.result)

