from nltk.stem import WordNetLemmatizer
import pickle


lemmatizer = WordNetLemmatizer()


# def make_skill_dict():
#     topics = open("test_files/finalDict.txt","r").read().split('\n\n')
#
#     # print(len(lines))
#     skill_dict = {}
#
#     for topic in topics:
#         par_skill = ''
#         for i,line in enumerate(topic.split('\n')):
#             if i == 0:
#                 par_skill = lemmatizer.lemmatize(line.strip().lower())
#                 # print("topic:",par_skill)
#             else:
#                 line = lemmatizer.lemmatize(line.strip().lower())
#                 if line in skill_dict:
#                     skill_dict[line].add(par_skill)
#                 else:
#                     skill_dict[line] = {par_skill}
#                 # print("skill:",line)
#         # print()
#
#     print("printing dict.......")
#     for key in skill_dict:
#         print(str(key).ljust(40) + str(skill_dict[key]).rjust(40))
#
#     pick_file = open("pickled_data/final_skill_dict_2.pickle","wb")
#     pickle.dump(skill_dict,pick_file)
#     pick_file.close()
#
#     return skill_dict


def load_skill_set():

    skill_dict = dict()
    pick_file = open("pickled_data/final_skill_dict_2.pickle", "rb")
    skill_dict = pickle.load(pick_file)
    pick_file.close()
    return skill_dict


def get_skill(skill_dic,topic):
    topic = lemmatizer.lemmatize(topic.strip().lower())
    if topic in skill_dic:
        return skill_dic[topic]
    else:
        return None


# skill_dict = make_skill_dict()
skill_dict = load_skill_set()

print(get_skill(skill_dict,'Sales Strategy'))
# while True:
#     inp = input("topic:")
#     print(get_skill(skill_dict,inp))
