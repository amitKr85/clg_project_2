from modules.enhanced_svo_extraction.subject_verb_object_extract import findSVOs, nlp
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

sample_text_1 = "Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a seemingly interminable ground test of the Apollo 1 spacecraft."
sample_text_2 = "CDIO (Conceive, Design, Implement, Operate) is one of the framework which has been introduced by mid 90's. The framework has been introduced to improve the technical skills among the engineering students. In Malaysia, this framework has been adopted in Malaysia on late 2000's by Taylor university, Universiti Teknologi Malaysia (UTM) and University Teknologi MARA (UiTM). However, there is a conflict while adopting CDIO since the Malaysia Education system in Institute of Higher Learning (IHL) and Engineering Accreditation Council (EAC) already adopted the OBE as core of implementation for education system. Hence, it is important to ensure that CDIO and OBE can complement each other to improve the graduate performance. This paper will propose the mapping of CDIO skills set and Program outcome (PO) of EAC so as to provide general guidelines for CDIO implementer to conform the need of EAC based on PO. The guidelines facilitate the CDIO implementer in Malaysia to provide a better approach of observing the PO attainment of graduate based on CDIO skills set."
sample_text_3 = "this is amit kumar. Ram is playing cricket. Hockey is being played by someone."
sample_text_4 = "OpenCV C++ Program for Face Detection. This program uses the OpenCV library to detect faces in a live stream from webcam or in a video file stored in the local machine. This program detects faces in real time and tracks it. It uses pre—trained XML classifiers for the same. The classifiers used in this program have facial features trained in them. Different classifiers can be used to detect different objects."
sample_text_5 = "The University of Illinois at Chicago Department of Bioengineering has modified several courses and has added courses to better prepare the Bioengineer for positions in the medical device, instruments, or supplies industry. The courses that have been modified fall under the categories of required, elective, undergraduate or graduate. Therefore all students have an opportunity to be trained in one or more of the job skill sets. The Bioengineering Curriculum has 6 courses designed to integrate at least one skill set into the course and 2 courses that have five (5) or more skill sets. Examples of skill sets are: Product Requirement Definition, Project Management, Project Scheduling, Status Reporting, Protocol Writing, Design Review, Hazard Analysis, and Risk Assessment. The classroom experience provides the student with training and a real life application of the skill set."
# tokens  = nlp(sample_text_2)

lemmatizer = WordNetLemmatizer()

vo_set = set()
stop_words = set(stopwords.words("english"))
sents = sent_tokenize(sample_text_5)
print(sents)
for sent in sents:
    tokens = nlp(sent)
    svos = findSVOs(tokens)
    print(svos)
    for subj,ver,obj in svos:

        tag_words = nltk.pos_tag(word_tokenize(obj))
        for word, tag in tag_words:
            # print(word+":",end="")
            if word in stop_words:
                obj = re.sub("\\b"+word+"\\b","",obj)
            elif not re.match(r"[A-Z]+",tag):
                obj = obj.replace(word,"")
        obj = obj.strip()
        obj = obj.replace("  "," ")
        if not obj.isspace() and len(obj)>0:
            vo_set.add((ver,obj))

print("final V-O dictionary....")
# print(vo_dic)
for item in vo_set:
    print(item)