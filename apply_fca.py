"""from concepts import Context

c = Context.fromstring('''
           |human|knight|king |mysterious|
King Arthur|  X  |  X   |  X  |          |
Sir Robin  |  X  |  X   |     |          |
holy grail |     |      |     |     X    |
''')

print(c.intension(['King Arthur', 'Sir Robin']))
"""
"""
import os,glob
from nltk.stem import WordNetLemmatizer
from xlwt import Workbook

lemmatizer = WordNetLemmatizer()
wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1",cell_overwrite_ok=True)
path = r'C:\\Users\AMIT\Downloads\whatsapp\tags\tags'
skills = set()

for filename in glob.glob(os.path.join(path, '*.txt')):
    temp_skills = open(filename,"r",encoding="utf-8").read().split(",")
    for skill in temp_skills:
        temp_skill = lemmatizer.lemmatize(skill.strip().lower())
        skills.add(temp_skill)

print(len(skills))
for row,skill in enumerate(skills):
    sheet1.write(row, 0, skill)
    print(row,skill)

wb.save("tech_skills_2.xls")
"""
"""
from concepts import Context

# c = Context.fromfile("test_files\\temp_formal_context.csv",frmat="csv",encoding="utf-8")
c = Context.fromfile("test_files\\water_bodies_formal_context.csv",frmat="csv",encoding="utf-8")
# print(c.intension(['king arthur', 'sir robin']))

for extent, intent in c.lattice:
    print("{} > {}".format(extent, intent))

c.lattice.graphviz(view=True)
"""

import pickle
import csv
import random
from concepts import Context
import matplotlib.pyplot as plt


# # reading tech skills
# pick_file = open("pickled_data/tech_skills.pickle","rb")
# skills = pickle.load(pick_file)
# pick_file.close()
# # print(len(skills))
#
# # taking first 10 skills an write it to csv
# csvfile = open("test_files/tech_formal_context.csv","w",newline="")
# csvwriter = csv.writer(csvfile)
#
# skills = list(skills)
# skills.insert(0,"")
# # print(skills)
# csvwriter.writerow(skills)
#
# for i in range(10):
#     row = []
#     row.append("project "+str(i+1))
#     for j in range(10):
#         row.append("X" if random.randint(0,1)>0 else "")
#     csvwriter.writerow(row)
#
# csvfile.close()


def generate_concept_matrix(filename, skill_list=None, render=False):
    # applying fca
    c = Context.fromfile(filename, frmat="csv")
    if render:
        c.lattice.graphviz(filename=filename.rstrip(".csv"), view=True)

    # reading csv headers
    csvfile = open(filename)
    csvreader = csv.reader(csvfile)

    # reading skills
    if skill_list is None:
        skill_list = csvreader.__next__()
        skill_list.pop(0)
    else:
        csvreader.__next__()

    # reading abstract names
    row_header = list()
    for row in csvreader:
        row_header.append(row[0])

    csvfile.close()

    # matrix to return
    mat = list()
    for i, concept in enumerate(c.lattice):
        extent, intent = concept
        print("c{} = {} > {}".format(i, extent, intent))
        row = list()
        for skill in skill_list:
            if skill in intent:
                row.append(1)
            else:
                row.append(0)
        for header in row_header:
            if header in extent:
                row.append(1)
            else:
                row.append(0)

        mat.append(row)

    return mat, row_header, skill_list


def refine_concept_matrix(mat, skills_len):
    i = 0
    while i < len(mat):
        conc = mat[i]
        flag = False
        for j in range(skills_len):
            if conc[j] == 1:
                flag = True
                break
        if not flag:
            mat.pop(i)
            continue
        flag = False
        for j in range(skills_len, len(conc)):
            if conc[j] == 1:
                flag = True
                break
        if not flag:
            mat.pop(i)
            continue
        i += 1


# concept matrix, row, column
tech_csv_path = "test_files/temp_tech_formal_context.csv"
stu_csv_path = "test_files/temp_student_formal_context.csv"

tasc, abstracts, skills = generate_concept_matrix(tech_csv_path)
refine_concept_matrix(tasc, len(skills))
print("abstract concept matrix")
for row in tasc:
    print(row)

tesc, students, skills = generate_concept_matrix(stu_csv_path, skills)
refine_concept_matrix(tesc, len(skills))

print("student concept matrix")
for row in tesc:
    print(row)


def generate_affinity_matrix(team_concept, task_concept, a=0, b=0, c=2, d=1):
    mat = [[0 for j in range(len(task_concept))] for i in range(len(team_concept))]

    for i in range(len(team_concept)):
        for j in range(len(task_concept)):
            for k in range(len(skills)):
                if team_concept[i][k] == 1 and task_concept[j][k] == 1:
                    mat[i][j] = mat[i][j] + a * team_concept[i][k]
                elif team_concept[i][k] == 0 and task_concept[j][k] == 0:
                    mat[i][j] = mat[i][j] + b
                elif team_concept[i][k] == 1 and task_concept[j][k] == 0:
                    mat[i][j] = mat[i][j] - c * team_concept[i][k]
                else:
                    mat[i][j] = mat[i][j] - d

    return mat


def generate_pref(mat, r_c_val, isRow=True):
    tup_list = list()
    for i in range(len(mat[0]) if isRow else len(mat)):
        if isRow:
            tup_list.append((mat[r_c_val][i], i))
        else:
            tup_list.append((mat[i][r_c_val], i))

    def sort_by_val(elem):
        return elem[0]

    sorted_list = sorted(tup_list, key=sort_by_val, reverse=True)

    pref_list = list()

    for val, i in sorted_list:
        pref_list.append(i)

    return pref_list


# hospital/resident problem
# pref_1 = hospital pref.   pref_2 = resident_pref.
def extended_sma(pref_1, pref_2):
    pairs = list()
    res_partner = dict()
    res_count_in_pref = len(pref_1.keys()) * len(pref_2.keys())

    while res_count_in_pref > 0:

        # for each hospital
        for h, pref in pref_1.items():
            # print("for h=",h)
            # for each resident in pref.
            for r in pref:
                # if already paired with ith hospital
                # print("for r=",r)
                if (h, r) in pairs:
                    # print("already found!")
                    continue
                elif r in res_partner:
                    # print("pair found n breaking")
                    pairs.remove((res_partner[r], r))
                    res_partner.pop(r)
                    res_count_in_pref += 1
                # print("paired",(h,r))
                pairs.append((h, r))
                res_partner[r] = h
                res_count_in_pref -= 1

                # for each successor h_ of h in r's pref. remove h_ and r from each other
                # using index from h+1 to end of r's pref
                # print("h found in r's pref. at ",pref_2[r].index(h),"len of r's pref. is",len(pref_2[r]))
                hpos = pref_2[r].index(h)
                for h_i in range(hpos + 1, len(pref_2[r])):
                    # print("removing h_(s) n r h_=",pref_2[r][hpos+1],"h_i=",h_i,"pref.=",pref_2[r])
                    # removing r from h_'s pref
                    pref_1[pref_2[r][hpos + 1]].remove(r)
                    res_count_in_pref -= 1
                    # removing h_ from r's pref
                    pref_2[r].pop(hpos + 1)

                break
        # check if any h's pref. still left with unallocated resident
        # if so then break
        # edit this //////////////////////////////////////////////////////////////////////////here////////
        # if len(res_partner.keys()) == len(pref_2.keys()):
        #     print("done quiting sma")
        #     break

    return pairs


print("---------------------------------------------------------------------------")
aff_mat = generate_affinity_matrix(tesc, tasc, 1, 1, 1, 1)
print("---------------------------------------------------------------------------")
print("aff mat")
for row in aff_mat:
    for val in row:
        print("{:3}".format(val), end="|")
    print()

# task concept preference
task_c_pref = dict()
# student concept preference
stu_c_pref = dict()

# print(generate_pref(aff_mat,0,False))
# generating pref order for student concepts
for stu_c_i in range(len(aff_mat)):
    stu_c_pref[stu_c_i] = generate_pref(aff_mat, stu_c_i, True)

print("---------------------------------------------------------------------------")
print("student preferences")
for k, v in stu_c_pref.items():
    print(k, v)

# generating pref order for abstract concepts
for task_c_i in range(len(aff_mat[0])):
    task_c_pref[task_c_i] = generate_pref(aff_mat, task_c_i, False)

print("project preferences")
for k, v in task_c_pref.items():
    print(k, v)

# h_pref = {0:[0,2,4,1,3], 1:[2,3,4,0,1], 2:[3,0,2,1,4]}
# r_pref = {0:[0,2,1], 1:[2,0,1], 2:[1,2,0], 3:[0,2,1], 4:[2,1,0]}
# task as hospital, students as residents
print("sma")
# pairss = extended_sma(h_pref,r_pref)
concept_pairs = extended_sma(task_c_pref, stu_c_pref)

print("---------------------------------------------------------------------------")
print("task_concept-student_concept pairs")
print(concept_pairs)

# analysing the correctness according to common skills
avg_stable_percentage = 0

for abst_con_i, stu_cons_i in concept_pairs:
    print("for pair (", abst_con_i, ",", stu_cons_i, ")")
    total_skill_pres = 0
    common_skill_pres = 0
    for i in range(len(skills)):
        if tasc[abst_con_i][i] == 1 and tesc[stu_cons_i][i] == 1:
            total_skill_pres += 1
            common_skill_pres += 1
        elif tasc[abst_con_i][i] == 1 or tesc[stu_cons_i][i] == 1:
            total_skill_pres += 1
    print("stable percentage:", 1 if total_skill_pres == 0 else common_skill_pres / total_skill_pres)
    avg_stable_percentage += 1 if total_skill_pres == 0 else common_skill_pres / total_skill_pres

print("---------------------------------------------------------------------------")
print("average stable percentage:", avg_stable_percentage / len(concept_pairs))
print("---------------------------------------------------------------------------")

project_part = dict()
student_part = dict()

for abst_con_i, stu_cons_i in concept_pairs:
    tasc_row = tasc[abst_con_i]
    tesc_row = tesc[stu_cons_i]

    proj_list = []
    stu_list = []

    for i in range(len(tasc_row)):
        if tasc_row[i] == 1:
            if i < len(skills):
                print(skills[i], end=" | ")
            else:
                print(abstracts[i - len(skills)], end=" | ")
                proj_list.append(i - len(skills))
    print(" > ", end="")
    for i in range(len(tesc_row)):
        if tesc_row[i] == 1:
            if i < len(skills):
                print(skills[i], end=" | ")
            else:
                print(students[i - len(skills)], end=" | ")
                stu_list.append(i - len(skills))

    for proj in proj_list:
        for stu in stu_list:
            if proj in project_part:
                project_part[proj].add(stu)
            else:
                project_part[proj] = {stu}

            if stu in student_part:
                student_part[stu].add(proj)
            else:
                student_part[stu] = {proj}
    print()

print("---------------------------------------------------------------------------")
print("project part ....")
for proj in sorted(project_part.keys()):
    print(abstracts[proj], "(", len(project_part[proj]), ")", ">", end="{")
    for s in project_part[proj]:
        print(students[s], end=",")
    print("}")

print("---------------------------------------------------------------------------")
print("student part ....")
for stus in sorted(student_part.keys()):
    print(students[stus], "(", len(student_part[stus]), ")", ">", end="{")
    for p in student_part[stus]:
        print(abstracts[p], end=",")
    print("}")

#############################################################################
import numpy as np
import pandas as pd

stu_skill_mat = np.array(pd.read_csv(stu_csv_path).replace([np.nan,'X'],[0, 1]).iloc[:,1:].values,dtype='int')
proj_skill_mat = np.array(pd.read_csv(tech_csv_path).replace([np.nan,'X'],[0,1]).iloc[:,1:].values,dtype='int')

proj_limit = 3
# print(stu_skill_mat)
# print(proj_skill_mat)

print("---------------------------------------------------------------------------")
for stu in sorted(student_part.keys(), key=lambda x: len(student_part[x]), reverse=True):
    if len(student_part[stu]) > proj_limit:
        # print("for",students[stu],">",student_part[stu])
        # list of tuples
        signif = []
        for proj in student_part[stu]:

            # check if project need stu
            # print(stu_skill_mat[stu,:],"::",proj_skill_mat[proj,:])
            if np.sum(np.bitwise_and(stu_skill_mat[stu,:],proj_skill_mat[proj,:])) <= 0:
                signif.append((proj, -10))
            # check if student have redundant or unique skills
            else:
                other_stu_list = list(project_part[proj])
                other_stu_list.remove(stu)
                other_stu_or_mat = np.sum(stu_skill_mat[other_stu_list,:],axis=0)
                # for i in range(len(other_stu_or_mat)):
                #     if other_stu_or_mat[i] > 0:
                #         other_stu_or_mat = 1
                #     else:
                #         other_stu_or_mat = 0
                other_stu_or_mat[other_stu_or_mat > 0] = 1

                left_skills = stu_skill_mat[stu] - other_stu_or_mat
                left_skills[left_skills < 0] = 0
                # have unique skills
                if np.sum(np.bitwise_and(left_skills, proj_skill_mat[proj])) > 0:
                    # print("project",proj,"has",np.sum(np.bitwise_and(left_skills, proj_skill_mat[proj])),"unique skills")
                    signif.append((proj,len(skills)+1+np.sum(np.bitwise_and(left_skills, proj_skill_mat[proj]))))
                else:
                    comm_skill = np.bitwise_and(other_stu_or_mat,stu_skill_mat[stu])
                    # have redundant skills
                    # print("project",proj,"has",np.sum(comm_skill),"red. skills")
                    signif.append((proj,len(skills) - np.sum(comm_skill)))

        # print("sign=",signif)
        for proj, sig in sorted(signif,key=lambda x:x[1]):
            if len(student_part[stu]) <= proj_limit :
                break
            student_part[stu].remove(proj)
            project_part[proj].remove(stu)
        # print("new list for the student=",student_part[stu])


print("after limiting projects")
print("---------------------------------------------------------------------------")
print("project part ....")
for proj in sorted(project_part.keys()):
    print(abstracts[proj], "(", len(project_part[proj]), ")", ">", end="{")
    for s in project_part[proj]:
        print(students[s], end=",")
    print("}")

print("---------------------------------------------------------------------------")
print("student part ....")
for stus in sorted(student_part.keys()):
    print(students[stus], "(", len(student_part[stus]), ")", ">", end="{")
    for p in student_part[stus]:
        print(abstracts[p], end=",")
    print("}")
# reducing students if he involves in >2 projects

# tesc = Context.fromfile("test_files/temp_student_formal_context.csv", frmat="csv")

# c.lattice.graphviz(view=True,directory="outputs",filename="temp_tech_concept_lattice")
