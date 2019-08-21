import pickle
import urllib
import urllib.request as url
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
#from dict import v_set
import bleach
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#from dict import *
import time
#from synoskill import sksyno
skillobj = set()
skilldict = set()
#syno = set(["expertise", "skilfulness", "expertness", "adeptness", "adroitness", "deftness", "dexterity", "ability", "prowess", "mastery", "competence", "competency", "capability", "efficiency", "aptitude", "artistry", "art", "finesse", "flair", "virtuosity", "experience", "professionalism", "talent", "cleverness", "smartness", "ingenuity", "versatility", "knack", "readiness", "handiness"])
def allletter(s,str):
    for c in s:
        if c ==' ':
            continue
        if c not in str:
            return 0
    return 1

str="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "


skill_set_file = open("pickled_data/final_skill_dict_2.pickle","rb")
# skill_set is a set() containing skills from linkedIn and wiki
counter =0
skill_set = pickle.load(skill_set_file)
for skill in skill_set:
    if counter < 80 and allletter(skill,str):
      #  print(skill)
        skilldict.add(skill)
    counter = counter + 1

for dic in skilldict:
    print(dic)



skill_set_file.close()




'''''
global stop_words
stop_words = set(stopwords.words('english'))

v2_set = set()
import requests

#url = raw_input("en.wikipedia.org/wiki")

for v in skill_set:
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
        for wo in sksyno:
            if wo.lower() == word.lower():
                skilldict.add(wo)
            else:
                skillobj.add(wo)



print('--------------------skilldictionary-------------------')
for sw in skilldict:
    print(sw)
print('---------------objectdictionary---------------')

for so in objdict:
    print(so)
'''''


















































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

