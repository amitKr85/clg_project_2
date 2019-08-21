import random
import pickle
import csv

csvfile = open("testing/student_formal_context_4.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)

# table = list()
pick_file = open("testing/all_skills.pickle","rb")
skills = list(pickle.load(pick_file))
pick_file.close()

col = len(skills)
# col_headers = [str(i) for i in range(col)]
no_of_students = 4

# for i in range(no_of_students):
#     val = random.randint(1, 2**col-1)
#     # print("for row",i,"val=",val)
#     row = list()
#     for j in range(col):
#         row.insert(0, 1 if ((val & (1 << j)) > 0) else 0)
#     table.append(row)

header_row = list(skills)
header_row.insert(0,"")
print("header len",len(header_row))
csvwriter.writerow(header_row)

for i in range(no_of_students):
    row = list()
    row.append("student" + str(i + 1))
    for j in range(col):
        row.append("X" if random.random() > 0.99 else "")
    # if random.randint(0,10) > 5:
    #     row.append("student"+str(i+1))
    #     total_skill = random.randint(1,10)
    #     for j in range(col):
    #         hv_skill = random.randint(0,1)
    #         if hv_skill == 1 and total_skill > 0:
    #             row.append("X")
    #             total_skill -= 1
    #         else:
    #             row.append("")
    # else:
    #     total_skill = random.randint(1, 10)
    #     for j in range(col):
    #         hv_skill = random.randint(0, 1)
    #         if hv_skill == 1 and total_skill > 0:
    #             row.insert(0,"X")
    #             total_skill -= 1
    #         else:
    #             row.insert(0,"")
    #
    #     row.insert(0, "student" + str(i + 1))
    # row.append("student"+str(i+1))
    # for j in range(col):
    #     row.append()
    print("row len",len(row))
    # table.append(row)
    csvwriter.writerow(row)

csvfile.close()

# # printing headers
# print("".ljust(len("s"+str(no_of_students))), end="")
# for skill in skills:
#     print(skill,end=",")
#
# # printing student values
# for i in range(no_of_students):
#     print()
#     print(("s"+str(i)).ljust(len("s"+str(no_of_students))),end="")
#     for c,j in enumerate(table[i]):
#         print(str(j).center(len(skills[c])+1),end="")
