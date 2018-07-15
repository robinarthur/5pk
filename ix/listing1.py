import sys
import pandas as pd
import sklearn
import spacy
import gensim
 
!{sys.executable} -m spacy download de
nlp = spacy.load('de')
doc = nlp("Alle Tools sind richtig installiert")
spacy.displacy.render(doc, style='dep', jupyter=True)
