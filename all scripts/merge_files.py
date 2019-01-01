from os import listdir
from os.path import isfile,join

# abstracts are seprated by #####

mypath = r'C:\Users\AMIT\Downloads\project_abstracts\big data'
# files = [ file_name
#           for file_name in listdir(mypath) if isfile(join(mypath, file_name)) and file_name.lower().endswith('.txt') ]
#
# final_file = open(join(mypath,"merged_bd_abstracts.txt"),"w",encoding="utf-8")
final_file = open(join(mypath,"merged_bd_abstracts.txt"),"r",encoding="utf-8")
print(len(final_file.read().split('#####')))
# for i,fil in enumerate(files):
#     abst = open(join(mypath,fil),encoding="utf-8").read()
#     final_file.write(abst)
#     if i != len(files)-1:
#         final_file.write('#####')
