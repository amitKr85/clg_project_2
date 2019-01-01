from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import nltk
import pickle


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


def make_skill_dict():
    topics = open("test_files/finalDict.txt","r").read().split('\n\n')

    # print(len(lines))
    skill_dict = {}

    for topic in topics:
        topic_words = []
        for i,line in enumerate(topic.split('\n')):
            if i == 0:
                print("for topic",line)
                for top_word in line.split(' '):
                    if top_word.strip().isalpha():
                        word = top_word.strip().lower()
                        wordnet_pos = get_wordnet_pos(nltk.pos_tag([word])[0][1])
                        if wordnet_pos == '':
                            word = lemmatizer.lemmatize(word)
                        else:
                            word = lemmatizer.lemmatize(word,wordnet_pos)

                        if word != 'skill' and word not in stop_words:
                            topic_words.append(word)
                            print(word,"added")
            else:
                print("for sbtop",line)
                for topic_word in topic_words:
                    print("for topic word",topic_word," sub_top addred",line)
                    if topic_word in skill_dict:
                        skill_dict[topic_word].add(line.lower().strip())
                    else:
                        skill_dict[topic_word] = {line.lower().strip()}
                for sub_top_word in line.split(' '):
                    if sub_top_word.strip().isalpha():
                        word = sub_top_word.strip().lower()
                        wordnet_pos = get_wordnet_pos(nltk.pos_tag([word])[0][1])
                        if wordnet_pos == '':
                            word = lemmatizer.lemmatize(word)
                        else:
                            word = lemmatizer.lemmatize(word, wordnet_pos)

                        if word != 'skill' and word not in stop_words:
                            if word in skill_dict:
                                skill_dict[word].add(line.lower().strip())
                            else:
                                skill_dict[word] = {line.lower().strip()}

        print()

    print("printing dict.......")
    for key in skill_dict:
        print("for key=",key)
        for item in skill_dict[key]:
            print(item)

    pick_file = open("pickled_data/final_skill_dict.pickle","wb")
    pickle.dump(skill_dict,pick_file)
    pick_file.close()

    return skill_dict

def load_skill_set():

    skill_dict = dict()
    pick_file = open("pickled_data/final_skill_dict.pickle", "rb")
    skill_dict = pickle.load(pick_file)
    pick_file.close()
    return skill_dict


# skill_dict = make_skill_dict()
skill_dict = load_skill_set()

def get_skills(skill_dic,topic):

    print("getting skill set for ",topic)
    skill_set = set()
    for word in topic.split(' '):
        print("for word=",word)
        if word.strip().isalpha():
            word = word.strip().lower()
            wordnet_pos = get_wordnet_pos(nltk.pos_tag([word])[0][1])
            if wordnet_pos == '':
                word = lemmatizer.lemmatize(word)
            else:
                word = lemmatizer.lemmatize(word, wordnet_pos)

            try:
                curr_skill_set = skill_dic[word]
                print("skill set=",curr_skill_set)
                if len(skill_set) == 0:
                    skill_set = curr_skill_set
                else:
                    skill_set = skill_set.intersection(curr_skill_set)

                print("intersection=",skill_set)
            except KeyError as e:
                print("no skill set found",e)

    return skill_set


print(get_skills(skill_dict,'communication development'))


# while True:
#     inp = input("input:")
#     inp = inp.lower().strip()
#     wordnet_pos = get_wordnet_pos(nltk.pos_tag([inp])[0][1])
#     if wordnet_pos == '':
#         inp = lemmatizer.lemmatize(inp)
#     else:
#         inp = lemmatizer.lemmatize(inp, wordnet_pos)
#
#     try:
#         print(skill_dict[inp])
#     except Exception as e:
#         print("nothing found",e)