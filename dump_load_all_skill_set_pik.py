import urllib.request
from bs4 import BeautifulSoup
import re
import pickle

# skill_file = open(r"arhived_modules\LinkedIn-Skills-Crawler-master\output\all_skills.txt","r",encoding="utf-8")
# # skill_file  = open("sample.txt","r")
# skills = skill_file.read().split('\n')
#
# skill_set = set()
#
# for skill in skills:
#     print(skill)
#     skill_set.add(skill.lower())
#
#
# def load_skill_dic():
#     skill_dic_file = open("pickled_data/skill_dic.pickle","rb")
#     skill_list = pickle.load(skill_dic_file)
#     skill_dic_file.close()
#     return skill_list
#
#
# skill_list = load_skill_dic()
#
# for skill in skill_list:
#     skill_set.add(skill.lower())
#
# skill_set_file = open("pickled_data/all_skill_set.pickle","wb")
# pickle.dump(skill_set,skill_set_file)
# skill_set_file.close()

skill_set_file = open("pickled_data/all_skill_set.pickle","rb")
skill_set = pickle.load(skill_set_file)
skill_set_file.close()

while True:
    st = input("skill:")
    print(st.lower() in skill_set)