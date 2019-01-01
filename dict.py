import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import wikipedia
v_set = set()
global stop_words
stop_words = set(stopwords.words('english'))
def get_words_from_string(s):
    return set(re.findall(re.compile('\w+'), s.lower()))

def get_words_from_file(fname):
    with open(fname, 'rb') as inf:
        return get_words_from_string(inf.read())

def main():
    global stop_words
    f= open("test_files/linkedin_all_skills.txt","rt",encoding="utf-8")
    if f.mode == 'rt':
       contents =f.read()
       wordList = contents.split()
       word1=word_tokenize(contents)

    fl =f.readlines()
    for word in word1:
        if word not in stop_words and word.__len__()>3:
            t=word.lower()
            #original = t
            #removed = original.replace("-", " ")
            if not t.isdigit() and t.isalpha():
               v_set.add(t)
       # v_set.add('discrete wavelet transform')
        #v_set.add('time series')


           # print(t)


    print('-----------------------------------------------------------------')

    temp = list(v_set)
    for w in temp:
        print(w)
#if __name__== "__main__":
main()