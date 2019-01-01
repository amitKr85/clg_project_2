import re
import urllib.request
from bs4 import BeautifulSoup
from custom_tree import *
from pptree import print_tree
import pydot
import pickle
import time

from sys import setrecursionlimit
setrecursionlimit(10000)

domain = "https://en.wikipedia.org"
base_page = "/wiki/Category:Skills"
# base_page = "/wiki/Category:Games_of_physical_skill" # this

# base_page = "/wiki/Category:Saint_Christopher%E2%80%93Nevis%E2%80%93Anguilla"
# base_page = "/wiki/Category:Procedural_knowledge"
# html = urllib.request.urlopen(domain+base_page)
# soup = BeautifulSoup(html,features="lxml")
# data = soup.findAll(text=True)


# skill_list = {}
skill_href_list = {}
max_lvl = None
t_to_sleep = time.time() + 30
t_to_save = time.time() + 300
target_pickle_file = "skills_lvl_3.pickle" # this
# pickle_file = open("pickled_data/root_tree_no_lvl.pickle","wb")


def scrap_url(rel_add, parent=None, lvl=0, pdomain=domain, proot=None):
    if max_lvl is not None:
        if lvl > max_lvl:
            return

    # to sleep after every 30 secs
    # global t_to_sleep
    # if time.time() > t_to_sleep:
    #     print("sleeping for 5 second, total running time:",time.perf_counter()/60,"minutes")
    #     time.sleep(5)
    #     t_to_sleep = time.time() + 30
    time.sleep(0.5)

    # to save data after every 5 mins
    global t_to_save
    if time.time() > t_to_save:
        pickle_file = open("pickled_data/"+target_pickle_file, "wb")
        pickle.dump(proot, pickle_file)
        pickle_file.close()
        print("pickled partial data up till ", parent)
        print("total running time:", time.perf_counter() / 60, "minutes")
        t_to_save = time.time() + 300

    html = None
    try:
        html = urllib.request.urlopen(pdomain + rel_add)
    except Exception as e:
        print("Exception occured opening url ",e)
        return
    soup = BeautifulSoup(html, features="lxml")
    sub_cat_sec = soup.find(id="mw-subcategories") # and mw-pages
    rel_cat_sec = soup.find(id="mw-pages")

    if rel_cat_sec is not None:
        anchors = rel_cat_sec.find_all('a')
        for anchor in anchors:
            if anchor.text == "learn more":
                continue
            el = Element(anchor.text.lower(), anchor.get('href'))
            parent.add_rel_cat(el)

    if sub_cat_sec is not None:
        anchors = sub_cat_sec.find_all('a')
        # print(anchors)
        for anchor in anchors:

            #### to show current anchor
            print(lvl,":",anchor)
            ####
            el = Element(anchor.text.lower(),anchor.get('href'))
            n = Node(el)

            #### to check and show if skill name is repeated
            # if anchor.text not in skill_list:
            #     skill_list[anchor.text] = 1
            # else:
            #     skill_list[anchor.text] += 1
            #     print("skill repeated :",anchor.text,":",skill_list[anchor.text],end="")
            #     temp = parent
            #     while not temp is None:
            #         print(temp.title,">",end="")
            #         if len(temp.parents)>0:
            #             temp = temp.parents[0]
            #         else:
            #             temp = None
            #     print()
            #### to check and show if same skill page is repeated

            if anchor.get('href') not in skill_href_list:
                skill_href_list[anchor.get('href')] = n
            else:
                print("skill link repeated :", anchor.get('href'), ":", skill_href_list[anchor.get('href')], end="")
                ####
                # if link is repeating
                # use existing object and append it to current parent and change the parent of the node
                # and dont call recursive for the link
                tempn = skill_href_list[anchor.get('href')]
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
            scrap_url(el.link,n,lvl=lvl+1,proot=proot)

        parent.isLeaf = False
    else:
        parent.isLeaf = True


def crawl_fresh(lvl=None):
    if lvl is not None:
        global max_lvl
        max_lvl = lvl

    root = Node(Element("skills",base_page)) # this

    st = time.perf_counter()
    try:
        scrap_url(base_page, root, proot=root)
    except Exception as e:
        print("Exception ocuured in fn ",e)
    et = time.perf_counter()


    print("DONE !!, time :",et-st)
    #
    pickle_file = open("pickled_data/"+target_pickle_file,"wb")
    pickle.dump(root,pickle_file)
    pickle_file.close()


    print("final pickled !!")
    return root


def load_root():
    pickle_file = open("pickled_data/"+target_pickle_file,"rb")
    root = pickle.load(pickle_file)
    pickle_file.close()
    print("pickle loaded")
    return root


# root = crawl_fresh(3)
root = load_root()
#
# root.traverse()
# print_tree(root,"childrens")


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


# skill_list = {}
# add_skills(root)
# skill_dic_file = open("pickled_data/skill_dic.pickle","wb")
# pickle.dump(skill_list,skill_dic_file)
# skill_dic_file.close()
def load_skill_dic():
    skill_dic_file = open("pickled_data/skill_dic.pickle","rb")
    skill_list = pickle.load(skill_dic_file)
    skill_dic_file.close()
    return skill_list


skill_list = load_skill_dic()

for key in skill_list:
    print(key)
# sel_parents = list()


# def find_all_parent(root,print_val=''):
#     print_val += ' > '+str(root)
#     print("called for ",root," no of parents:",len(root.parents))
#     for parent in root.parents:
#         find_all_parent(parent,print_val)
#     if str(root) == 'Skills':
#         sel_parents.append(print_val)
#
#
# def find_all_roots(skill):
#     try:
#         leaves = skill_list[skill]
#         print(len(leaves))
#         for leave in leaves:
#             find_all_parent(leave)
#     except KeyError as err:
#         print("no key found",err)
#
#
# find_all_roots('Parkour')
# print("len",len(sel_parents)," set len",len(set(sel_parents)))
# for l in sel_parents:
#     print(l)

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

# for skill in skill_list:
#     print(skill)
