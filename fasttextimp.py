import fasttext

# model = fasttext.train_supervised('train_data.txt',epoch=50,lr=0.5,loss='ova')
# model.save_model("fasttext_classifier.bin")
model = fasttext.load_model("fasttext_classifier.bin")
# print(model.words)
print(model.predict("Using Support Vector Machines to Classify Student Attentiveness for the Development of Personalized Learning Systems",k=100,threshold=0.3))
