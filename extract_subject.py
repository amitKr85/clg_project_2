from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords,state_union
import nltk
import re

# sample texts
sample_text_1 = "CDIO (Conceive, Design, Implement, Operate) is one of the framework which has been introduced by mid 90's. The framework has been introduced to improve the technical skills among the engineering students. In Malaysia, this framework has been adopted in Malaysia on late 2000's by Taylor university, Universiti Teknologi Malaysia (UTM) and University Teknologi MARA (UiTM). However, there is a conflict while adopting CDIO since the Malaysia Education system in Institute of Higher Learning (IHL) and Engineering Accreditation Council (EAC) already adopted the OBE as core of implementation for education system. Hence, it is important to ensure that CDIO and OBE can complement each other to improve the graduate performance. This paper will propose the mapping of CDIO skills set and Program outcome (PO) of EAC so as to provide general guidelines for CDIO implementer to conform the need of EAC based on PO. The guidelines facilitate the CDIO implementer in Malaysia to provide a better approach of observing the PO attainment of graduate based on CDIO skills set."
sample_text_2 = "The University of Illinois at Chicago Department of Bioengineering has modified several courses and has added courses to better prepare the Bioengineer for positions in the medical device, instruments, or supplies industry. The courses that have been modified fall under the categories of required, elective, undergraduate or graduate. Therefore all students have an opportunity to be trained in one or more of the job skill sets. The Bioengineering Curriculum has 6 courses designed to integrate at least one skill set into the course and 2 courses that have five (5) or more skill sets. Examples of skill sets are: Product Requirement Definition, Project Management, Project Scheduling, Status Reporting, Protocol Writing, Design Review, Hazard Analysis, and Risk Assessment. The classroom experience provides the student with training and a real life application of the skill set."
sample_text_3 = "The disjunctive model of skill map in knowledge spaces can be interpreted based on an or-binary relation table between skills and questions. There may exist skills that are the union of other skills. Omitting these skills will not change the knowledge structure. Finding a minimal skill set may be formulated similar to the problem of attribute reduction in rough set theory, where an and-binary relation table is used. In this paper, an or-relation skill-question table is considered for a disjunctive model of knowledge spaces. A minimal skill set is defined and an algorithm for finding the minimal skill set is proposed. An example is used to illustrate the basic idea."
sample_text_4 = 'The little cat sat on the mat. She was trying to escape.'
sample_text_5 = state_union.raw('2006-GWBush.txt')

# tokenized sentences
sents = sent_tokenize(sample_text_4)
# stop words
stop_words = set(stopwords.words('english'))

# for every sentence in para.
for sent in sents:

    # tokenize and tag words
    words = word_tokenize(sent)
    tagged = nltk.pos_tag(words)

    # filter tagged words
    # tagged = [ (word,tag) for word,tag in tagged if re.match(r'[VN][A-Z]*',tag) and word not in stop_words ]
    # printing filtered tagged words
    print(tagged)

    # pattern for extracting subjects
    chunk_gram = r'''Chunk: {(<NN>|<PRP>)}<.*>*<VB.*>*<.*>*<NN>*
                            {<VB.*>}
                            '''
    chunk_parser = nltk.RegexpParser(chunk_gram)

    # extracted subjects in form of tree
    chunked = chunk_parser.parse(tagged)
    chunked.draw()

    # printing subjects
    # for subtree in chunked.subtrees(filter=lambda t :t.label() =='SUBJECT'):
    #     subs = [ word for word,tag in subtree.leaves()]
    #     print("subject:",subs)