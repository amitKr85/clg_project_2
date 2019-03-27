from concepts import Context
import csv


def generate_concept_matrix(filename, skill_list=None, render=False):
    # applying fca
    c = Context.fromfile(filename, frmat="csv")
    if render:
        c.lattice.graphviz(filename=filename.rstrip(".csv"), view=True)

    # reading csv headers
    csvfile = open(filename)
    csvreader = csv.reader(csvfile)

    # reading skills
    if skill_list is None:
        skill_list = csvreader.__next__()
        skill_list.pop(0)
    else:
        csvreader.__next__()

    # reading abstract names
    row_header = list()
    for row in csvreader:
        row_header.append(row[0])

    csvfile.close()

    # matrix to return
    mat = list()
    for i, concept in enumerate(c.lattice):
        extent, intent = concept

        # skip for non-significant concept
        if len(extent) == 0 or len(intent) == 0:
            continue

        print("c{} = {} > {}".format(i, extent, intent))
        row = list()
        for skill in skill_list:
            if skill in intent:
                row.append(1)
            else:
                row.append(0)
        for header in row_header:
            if header in extent:
                row.append(1)
            else:
                row.append(0)

        mat.append(row)

    return mat, row_header, skill_list


# def refine_concept_matrix(mat, skills_len):
#     i = 0
#     while i < len(mat):
#         conc = mat[i]
#         flag = False
#         for j in range(skills_len):
#             if conc[j] == 1:
#                 flag = True
#                 break
#         if not flag:
#             mat.pop(i)
#             continue
#         flag = False
#         for j in range(skills_len, len(conc)):
#             if conc[j] == 1:
#                 flag = True
#                 break
#         if not flag:
#             mat.pop(i)
#             continue
#         i += 1
