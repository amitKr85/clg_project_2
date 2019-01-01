from nltk.stem import WordNetLemmatizer
from pptree import print_tree
from print_tree_to_file import print_tree_to_file


class Node:

    def __init__(self, value=None, childrens=None):
        self.value = value
        if childrens is not None:
            self.childrens = childrens
        else:
            self.childrens = list()

    def add_children(self, children):
        self.childrens.append(children)

    def __str__(self):
        return self.value


lemmatizer = WordNetLemmatizer()
leave_dict = {}
topics_root = {}


def traverse_topic():
    topics = open("test_files/finalDict.txt", "r").read().split('\n\n')

    for topic in topics:
        parent = None
        for i, line in enumerate(topic.split('\n')):
            line = lemmatizer.lemmatize(line.strip().lower())
            if i == 0:
                if line in leave_dict and leave_dict[line] is not True:
                    leave_dict[line] = False
                parent = line

            else:
                leave_dict[line] = True
                if parent in topics_root:
                    topics_root[parent].add(line)
                else:
                    topics_root[parent] = {line}


def is_topic_leave(topic):
    topic = lemmatizer.lemmatize(topic.strip().lower())

    if topic in leave_dict:
        return leave_dict[topic]
    else:
        return False


def make_hierarchy_util(parent, key, visited):
    if visited.get(key, False):
        return

    new_node = Node(key)
    parent.add_children(new_node)
    visited[key] = True

    try:
        subset = topics_root[key]
        for key2 in subset:
            make_hierarchy_util(new_node, key2, visited)

    except KeyError as e:
        print("err:", e)

    visited[key] = False


def make_hierarchy():
    hroot = Node("root")
    visited = {}
    for key in topics_root:
        if not is_topic_leave(key):
            make_hierarchy_util(hroot, key, visited)

    return hroot


if __name__ == '__main__':
    traverse_topic()
    root = make_hierarchy()
    file = open("output_trees/hierarchy.txt", "w", encoding="utf-8")
    print_tree_to_file(root, "childrens", file_to_print=file)