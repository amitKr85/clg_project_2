import csv
import pickle

csvfile = open("test_files/tech_formal_context.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)

# tech skills
pick_file = open("pickled_data/tech_skills.pickle","rb")
skills = pickle.load(pick_file)
pick_file.close()

# writing heading row
skills = list(skills)
skills.insert(0,"")
# print(skills)
csvwriter.writerow(skills)

file = open("test_files/abstracts_skills_table.txt","r",encoding="utf-8")

rows = file.read().split("\n")

# print(len(rows[0]))
for i,row in enumerate(rows):
    cols = row.split("\t")[:len(skills)]
    cols[0] = "abstract"+str(i+1)
    for i in range(1,len(cols)):
        cols[i] = "X" if cols[i] == "1" else ""
    print(cols)
    csvwriter.writerow(cols)

csvfile.close()
