# clg_project

# project to make hierarchy of projects and distribute the work among participants according to their skills
# implemented in python 3.x

Important instructions in order to use the programs
# image_to_test_corr.py
    A program to extract texts from given image and correct the uncorrect extracted words
    # before use image_to_test_corr.py do following few things
        for OCR or extracting text from image
          1. install teserract from here https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe and then use command in cmd : pip install pytesserract
        for text correction 
          1. install spellchecker throungh cmd: pip install pyspellchecker
        for extracting nouns
          1. install textblob : pip install textblob
          
# extract_subject.py
    Program to extract subjects from given paragraph
    # before use extract_subject.py please make sure you have downloaded all nltk packages by below commands in python shell
        >>import nltk
        >>nltk.download()

# extract_verb_obj_dict.py
    Program to extract verb_object pairs from given paragraph
    # before use extract_verb_object_dictionary
        Install spacy and download en ('english') package. 
        Download english package through command in cmd(as administrator): python -m spacy download en

# crawl_wiki.py
    Program to crawl skill categories from wiki pages and make a graph structure from the collected skills
    Using custom_tree.py to make tree structure
    # before using this program
        Install graphviz, pydot to visualize the graph
        Install pptree to visualize it as a tree
