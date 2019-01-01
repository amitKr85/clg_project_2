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
from test1 import skilldict
#import urllib2
from dict import *
import time
#from synoskill import sksyno
corrskdic = set()
baseURL = "http://en.wikipedia.org/wiki/"

for v in skilldict:
   if " skill" in v.lower() or " skill " in v.lower():
       corrskdic.add(v)
   else:
       original = v
       removed = original.replace("-", " ")
       time.sleep(.5)
       print('------------------------------------------', v, '-----------------------')
       article = removed
       # print(article)
       article = quote(article)

       fullURL = baseURL + article
       # print fullURL
       try:
           # req = urllib.Request(fullURL)
           resp = urlopen(fullURL)
           if resp.getcode() == 404:

               # Do whatever you want if 404 is found
               print("404 Found!")
           else:
               # Do your normal stuff here if page is found.
               print("URL: {0} Response: {1}".format(fullURL, resp.getcode()))
               corrskdic.add(v)
               # corrskdic.add(orignal)


       except:
           print("Could not connect to URL: {0} ".format(fullURL))

for i in corrskdic:
    print(i)