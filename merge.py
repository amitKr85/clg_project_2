import os
import nltk
import re

abstract_files = os.listdir("abstract/")
tag_files = os.listdir("tags/")

print(abstract_files)
print(tag_files)
train_data = ""
for i in range(len(abstract_files)):
	abstract = open("abstract/"+abstract_files[i],"r").read()
	abstract = ' '.join([re.sub(r'\W',"",word).lower() for word in nltk.word_tokenize(abstract)])
	abstract = re.sub(r"  "," ",abstract)
	tag_file = abstract_files[i][:-4]+'a.txt' if abstract_files[i][:-4].isdigit() else 's'+abstract_files[i][1:]
	tags = open("tags/"+tag_file,"r").read().split(',')
	tags = [ '__label__'+''.join([re.sub(r'\W',"",tok).capitalize() for tok in nltk.word_tokenize(tag)]) for tag in tags]
	print(i,str(tags)+":"+abstract)
	train_data+=' '.join(tags)+' '+abstract+'\n'

with open("train_data.txt","w") as file:
	file.write(train_data)
