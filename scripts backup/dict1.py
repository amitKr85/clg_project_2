import urllib
import urllib.request as url
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from dict import v_set
import bleach
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from dict import *
import time

global stop_words
stop_words = set(stopwords.words('english'))

v2_set = set()
import requests

#url = raw_input("en.wikipedia.org/wiki")

for v in v_set:
    original = v
    removed = original.replace("-", " ")
    time.sleep(.5)
    print('------------------------------------------',v,'-----------------------')
    article= removed
    #print(article)
    article = quote(article)
    from urllib.request import urlopen

    def find_bad_qn(a):
        url ="http://en.wikipedia.org/wiki/"+article
        try:
            urlopen(url)
        except:
            pass

   # print("Please Wait.. it will take some time")
    #for i in range(298314,298346):
     #   find_bad_qn(i)


    sauce=urllib.request.urlopen("http://en.wikipedia.org/wiki/"+article).read()
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
        print(word)


















































    #if  stop_words:
      #      print(word)

    #for para in :
     #   print(para.string)
    #data = r.text

    #soup = BeautifulSoup(data,'html.parser')
    #artist_name_list = soup.find(class_='BodyText')
    #print(soup.find(class_='BodyText'))
    #artist_name_list_items = artist_name_list.find_all('a')

    # Use .contents to pull out the <a> tag’s children
    #for artist_name in artist_name_list:
     #   names = artist_name.contents[0]
      #  print(names)

    #print(soup.find('div',id="bodyContent").p)

