from concepts import Context
import graphviz

SORTKEYS = [lambda c: c.index]

NAME_GETTERS = [lambda c: 'c%d' % c.index]


def show_graph(lattice, filename=None, directory=None, render=False, view=False, **kwargs):

    # """Return graphviz source for visualizing the lattice graph."""
    # dot = graphviz.Digraph(
    #     name=lattice.__class__.__name__,
    #     comment=repr(lattice),
    #     filename=filename,
    #     directory=directory,
    #     node_attr=dict(shape='circle', width='.25', style='filled', label=''),
    #     edge_attr=dict(dir='none', labeldistance='1.5', minlen='2'),
    #     **kwargs
    # )

    sortkey = SORTKEYS[0]

    node_name = NAME_GETTERS[0]

    nodecount = 0
    edgecount = 0
    for concept in lattice._concepts:
        name = node_name(concept)
        nodecount+=1
        # dot.node(name)
        print("for node =",name)

        if concept.objects:
            # dot.edge(name, name, headlabel=' '.join(concept.objects),labelangle='270', color='transparent')
            print("objects >",' | '.join(concept.objects))

        if concept.properties:
            # dot.edge(name, name, taillabel=' '.join(concept.properties), labelangle='90', color='transparent')
            print("properties >",' | '.join(concept.properties))
        # dot.edges((name, node_name(c)) for c in sorted(concept.lower_neighbors, key=sortkey))
        print("edges :")
        for i in sorted(concept.lower_neighbors,key=sortkey):
            print(name,"->",node_name(i))
            edgecount+=1

        print()
        print("nodes:",nodecount,"edges:",edgecount)

    # if render or view:
    #     dot.render(view=view)  # pragma: no cover
    # return dot


# c = Context.fromfile("test_files/tech_formal_context.csv",frmat="csv")
c = Context.fromfile("test_files/student_formal_context.csv",frmat="csv")
# max_e_len = 0
# for e,i in c.lattice:
#     if len(e) > max_e_len:
#         max_e_len = len(e)
for i,exin in enumerate(c.lattice):
    extent,intent = exin
    print("c"+str(i),">",extent,"\t->",intent)
#
# c.lattice.graphviz(view=True,filename="temp_show.pdf")

# show_graph(c.lattice,filename="temp_show.pdf",directory="output_trees",view=True)
