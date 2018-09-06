import docx  
from nltk import pos_tag, word_tokenize
import re

#function to get text from docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# function driver code
docxText = getText("test_files/abstracts.docx")

# all words  along with tags
allSamplePos=pos_tag(word_tokenize(docxText))

# words dictionary
words = {}

# loop through all sampled words
for word,pos in allSamplePos:
	# regex to mactch for only verbs and adjectives
	if re.match(r'[VJ][A-Z]*',pos):
		words[ word ] = pos

# prints all verbs and adjectives
print("all appeared verbs..\n")
for word in words:
	if re.match(r'[V][A-Z]*',words[word]):
		print(word)

print("\nall appeared adjectives..\n")
for word in words:
	if re.match(r'[J][A-Z]*',words[word]):
		print(word)
