# for image proccessing
from PIL import Image
# for extract text
from pytesseract import image_to_string
# for check spelling
from spellchecker import SpellChecker
import re
# for extract nouns
from textblob import TextBlob


print("extracting text from image....")
# extracted text from image 
text = image_to_string(Image.open(r'test_files\proj_desc_ss.png'))

print(text)

print("correcting words....")
# convert string into list of words
#wordList = re.sub("[^\\w]", " ",  text).split()
wordList = text.split()

# correcting misspelled word
spell = SpellChecker()
#misspelled = spell.unknown(wordList)
correctedText=''
for word in wordList:
	correctedText += spell.correction(word)+' '
	#print(spell.candidates(word))

print(correctedText)

print("extracting nouns....")
# extracting noun
blob = TextBlob(correctedText)
nounList = blob.noun_phrases

print(nounList)