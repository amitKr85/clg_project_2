class Element:
    def __init__(self,data,link=""):
        self.data = data
        self.link = link

    def __str__(self):
        return str(self.data)


class Node:

    def __init__(self,title=None,parents=None,rel_cat=None,childrens=None):

        self.title = title

        self.isLeaf = None

        if parents is None:
            self.parents = list()
        else:
            self.parents = parents

        if rel_cat is None:
            self.rel_cat = list()
        else:
            self.rel_cat = rel_cat

        if childrens is None:
            self.childrens = list()
        else:
            self.childrens = childrens

    # def __copy__(self,parent=None):
    #     n = Node(self.title,parent,self.rel_cat)
    #     return n

    def __str__(self):
        return str(self.title)

    def add_child(self,child):
        self.childrens.append(child)

    def add_parent(self,parent):
        self.parents.append(parent)

    def add_rel_cat(self,rel):
        self.rel_cat.append(rel)

    def has_parent(self,arg_parent):
        if str(self) == str(arg_parent):
            return True

        for parent in self.parents:
            if parent.has_parent(arg_parent) is True:
                return True

    def clear_parents(self):
        self.parents.clear()

    def clear_childrens(self):
        self.childrens.clear()

    def clear(self):
        self.clear_parents()
        self.clear_childrens()

    def traverse(self):
        print( self.title)
        # print("rel_cat:", self.rel_cat)
        # print("rel_cat:",end="")
        # for rel in self.rel_cat:
        #     print(rel,end=";")
        print("leaf ",self.isLeaf)
        for child in self.childrens:
            child.traverse()
