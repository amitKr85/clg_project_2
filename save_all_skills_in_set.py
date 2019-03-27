from nltk.stem import WordNetLemmatizer
import os
import glob
import pickle

non_tech_skills = set()

lemmatizer = WordNetLemmatizer()
topics = open("test_files/finalDict.txt","r").read().split('\n\n')

for topic in topics:
    # temp_skill = ''
    for line in topic.split('\n'):
        temp_skill = lemmatizer.lemmatize(line.strip().lower())
        non_tech_skills.add(temp_skill)

# saving all non-tech skills
print("total non-tech skills",len(non_tech_skills))
pick_file = open("pickled_data/non_tech_skills.pickle","wb")
pickle.dump(non_tech_skills,pick_file)
pick_file.close()

tech_skills = set()

path = r'C:\\Users\AMIT\Downloads\whatsapp\tags\tags'
for filename in glob.glob(os.path.join(path, '*.txt')):
    temp_skills = open(filename,"r",encoding="utf-8").read().split(",")
    for skill in temp_skills:
        temp_skill = lemmatizer.lemmatize(skill.strip().lower())
        # if "h/sup /spl infin// induced norm" in temp_skill:
        #     print(filename)
        tech_skills.add(temp_skill)


print("total tech skills",len(tech_skills))
# for skill in tech_skills:
#     print(skill)

# saving all tech-skills
pick_file = open("pickled_data/tech_skills.pickle","wb")
pickle.dump(tech_skills,pick_file)
pick_file.close()

# saving all skills
skills = non_tech_skills.union(tech_skills)
print("total skills",len(skills))

pick_file = open("pickled_data/all_skills.pickle","wb")
pickle.dump(skills,pick_file)
pick_file.close()


'''
pick_file = open("pickled_data/all_skills.pickle","rb")
skills = pickle.load(pick_file)
pick_file.close()
print(len(skills))
for skill in skills:
    print(skill)
'''

'''C:\\Users\AMIT\Downloads\whatsapp\tags\tags\'
'''
