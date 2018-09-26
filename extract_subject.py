from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords,state_union
import nltk
import re

# sample texts
sample_text_1 = "The disjunctive model of skill map in knowledge spaces can be interpreted based on an or-binary relation table between skills and questions. There may exist skills that are the union of other skills. Omitting these skills will not change the knowledge structure. Finding a minimal skill set may be formulated similar to the problem of attribute reduction in rough set theory, where an and-binary relation table is used. In this paper, an or-relation skill-question table is considered for a disjunctive model of knowledge spaces. A minimal skill set is defined and an algorithm for finding the minimal skill set is proposed. An example is used to illustrate the basic idea."
sample_text_2 = 'Hello this is Amit. I am here to tell you something about MIDI. Ram is playing cricket'
sample_text_3 = state_union.raw('2006-GWBush.txt')

# tokenized sentences
sents = sent_tokenize(sample_text_1)
# stop words
stop_words = set(stopwords.words('english'))

# for every sentence in para.
for sent in sents:

    # tokenize and tag words
    words = word_tokenize(sent)
    tagged = nltk.pos_tag(words)

    # filter tagged words
    tagged = [ (word,tag) for word,tag in tagged if re.match(r'[VN][A-Z]*',tag) and word not in stop_words ]
    # printing filtered tagged words
    print(tagged)

    # pattern for extracting subjects
    chunk_gram = r'''SUBJECT: {(<NN>|<NNP>)*}<.*>*<VB.*><.*>*<NN.*>'''
    chunk_parser = nltk.RegexpParser(chunk_gram)

    # extracted subjects in form of tree
    chunked = chunk_parser.parse(tagged)
    chunked.draw()

    # printing subjects
    for subtree in chunked.subtrees(filter=lambda t :t.label() =='SUBJECT'):
        subs = [ word for word,tag in subtree.leaves()]
        print("subject:",subs)
