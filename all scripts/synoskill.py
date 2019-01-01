from nltk.stem import WordNetLemmatizer
lzr = WordNetLemmatizer()
syno = set(["expertise", "skilfulness", "expertness", "adeptness", "adroitness", "deftness", "dexterity", "ability", "prowess", "mastery", "competence", "competency", "capability", "efficiency", "aptitude", "artistry", "art", "finesse", "flair", "virtuosity", "experience", "professionalism", "talent", "cleverness", "smartness", "ingenuity", "versatility", "knack", "readiness", "handiness"])
global sksyno

sksyno=set()

for d in syno:
    sksyno.add(lzr.lemmatize(d,pos='v'))
for s in sksyno:
    print(s)