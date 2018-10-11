import re
import urllib.request
from bs4 import BeautifulSoup
from custom_tree import *
from pptree import print_tree
import pydot
import pickle
import time

domain = "https://en.wikipedia.org"
base_page = "/wiki/Category:Skills"

skill_list = {}
skill_href_list = {}
max_lvl = 2

def scrap_url(rel_add,parent=None,lvl=0,pdomain=domain):
    if lvl > max_lvl:
        return
    html = urllib.request.urlopen(pdomain + rel_add)
    soup = BeautifulSoup(html, features="lxml")
    sub_cat_sec = soup.find(id="mw-subcategories") # and mw-pages
    rel_cat_sec = soup.find(id="mw-pages")

    if rel_cat_sec is not None:
        anchors = rel_cat_sec.find_all('a')
        for anchor in anchors:
            if anchor.text == "learn more":
                continue
            el = Element(anchor.text, anchor.get('href'))
            parent.add_rel_cat(el)

    if sub_cat_sec is not None:
        anchors = sub_cat_sec.find_all('a')
        # print(anchors)
        for anchor in anchors:
            #### to show current anchor
            print(anchor)
            ####
            el = Element(anchor.text,anchor.get('href'))
            n = Node(el)
            
            #### to check and show if same skill page is repeated
            if anchor.get('href') not in skill_href_list:
                skill_href_list[anchor.get('href')] = (1,n)
            else:
                skill_href_list[anchor.get('href')] = (skill_href_list[anchor.get('href')][0]+1,skill_href_list[anchor.get('href')][1])
                #### to show the all parent nodes
                print("skill link repeated :",anchor.get('href'),":",skill_href_list[anchor.get('href')][0],end="")
                ####
                # if link is repeating
                # use existing object and append it to current parent and change the parent of the node
                # and dont call recursive for the link
                tempn = skill_href_list[anchor.get('href')][1]
                # check whether the sub-category is already a parent
                # if True dont add as a child
                flag = parent.has_parent(tempn)
                if not flag:
                    parent.add_child(tempn)
                    tempn.add_parent(parent)
                else:
                    #### pass
                    print(parent,"Node is already Parent",tempn)
                    ####
                continue

            parent.add_child(n)
            n.add_parent(parent)
            scrap_url(el.link,n,lvl=lvl+1)


# root = Node(Element("Skills",base_page))
#
# t1 = time.perf_counter()
# scrap_url(base_page,root)
# t2 = time.perf_counter()
#
#
# print("DONE !!, time :",t2-t1)
# #
# pickle_file = open("pickled_data/root_tree_lvl1.pickle","wb")
# pickle.dump(root,pickle_file)
# pickle_file.close()
# print("pickled")
pickle_file = open("pickled_data/root_tree_lvl2.pickle","rb")
root = pickle.load(pickle_file)
pickle_file.close()
print("pickle loaded")

# root.traverse()
print_tree(root,"childrens")

skill_list = {}


def add_skills(root):

    if str(root) not in skill_list:
        skill_list[str(root)] = [root]
    else:
        l = skill_list[str(root)]
        if root not in l:
            l.append(root)

    for rel_cat in root.rel_cat:
        if str(rel_cat) not in skill_list:
            skill_list[str(rel_cat)] = [root]
        else:
            l = skill_list[str(rel_cat)]
            if root not in l:
                l.append(root)

    for children in root.childrens:
        add_skills(children)


add_skills(root)
sel_parents = list()


def find_all_parent(root,print_val=''):
    print_val += ' > '+str(root)
    print("called for ",root," no of parents:",len(root.parents))
    for parent in root.parents:
        find_all_parent(parent,print_val)
    if str(root) == 'Skills':
        sel_parents.append(print_val)


def find_all_roots(skill):
    try:
        leaves = skill_list[skill]
        print(len(leaves))
        for leave in leaves:
            find_all_parent(leave)
    except KeyError as err:
        print("no key found",err)


find_all_roots('Parkour')
print("len",len(sel_parents)," set len",len(set(sel_parents)))
for l in sel_parents:
    print(l)

# print("len",len(list_set))
# graph = pydot.Dot(graph_type='graph')
#
# def add_all_edge(graph,root):
#     for children in root.childrens:
#         graph.add_edge(pydot.Edge(str(root),str(children)))
#         add_all_edge(graph,children)
#
# add_all_edge(graph,root)
# graph.write('output_trees/output_lvl2.dot',encoding='utf-8')

# use this command in cmd to create .png file
# dot output.dot -Tpng -o output.png
