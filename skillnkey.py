from urllib.request import urlopen
import pickle
import urllib
import urllib.request as url
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from dict import v_set
import bleach
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#from test1 import skilldict
#import urllib2
from dict import *
import time
from synoskill import sksyno
from filterurldict import corrskdic
skillobj = set()
skilldic = set()

global stop_words
stop_words = set(stopwords.words('english'))

v2_set = set()
import requests

baseURL = "http://en.wikipedia.org/wiki/"

for v in corrskdic:
    original = v
    removed = original.replace("-", " ")
    time.sleep(.5)
    print('------------------------------------------',v,'-----------------------')
    article= removed
    #print(article)
    article = quote(article)
    from urllib.request import urlopen

    def find_bad_qn(a):
        url = baseURL + article
        try:
            urlopen(url)
        except:
            pass

#    print("Please Wait.. it will take some time")
 #   for i in range(298314,298346):
  #      find_bad_qn(i)


    sauce=urllib.request.urlopen(baseURL +article).read()
    soup=bs(sauce,'lxml')
    vo_set = set()
    w1=soup.find(attrs={'class':'mw-parser-output'})
    #bleach.clean(w1, tags=[], attributes={}, styles=[], strip=True)
    w2=w1.text

    w3=word_tokenize(w2)


    #print(w1.text)
    for word in w3:
        if word not in stop_words and word.__len__()>3 and word.isalpha():
            vo_set.add(word)

    for word in vo_set:
        for wo in sksyno:
            if wo.lower() == word.lower():
                skilldic.add(v)
            else:
                skillobj.add(v)
print('------authentic skilldict------------------')
for j in skilldic:
    print(j)
print('------------keyword dictionary---------------')
for k in skillobj:
    print(k)