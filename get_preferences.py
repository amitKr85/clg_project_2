def generate_affinity_matrix(team_concept, task_concept, skills, a, b, c, d):
    
    mat = [[0 for j in range(len(task_concept))] for i in range(len(team_concept))]

    for i in range(len(team_concept)):
        for j in range(len(task_concept)):
            for k in range(len(skills)):
                if team_concept[i][k] == 1 and task_concept[j][k] == 1:
                    mat[i][j] = mat[i][j] + a * team_concept[i][k]
                elif team_concept[i][k] == 0 and task_concept[j][k] == 0:
                    mat[i][j] = mat[i][j] + b
                elif team_concept[i][k] == 1 and task_concept[j][k] == 0:
                    mat[i][j] = mat[i][j] - c * team_concept[i][k]
                else:
                    mat[i][j] = mat[i][j] - d

    return mat


def generate_pref(mat, r_c_val, is_row=True):
    
    tup_list = list()
    for i in range(len(mat[0]) if is_row else len(mat)):
        if is_row:
            tup_list.append((mat[r_c_val][i], i))
        else:
            tup_list.append((mat[i][r_c_val], i))

    def sort_by_val(elem):
        return elem[0]

    sorted_list = sorted(tup_list, key=sort_by_val, reverse=True)

    pref_list = list()

    for val, i in sorted_list:
        pref_list.append(i)

    return pref_list


def get_preferences(team_concept, task_concept, skills, a=1, b=0.5, c=0.5, d=0):
    
    aff_mat = generate_affinity_matrix(team_concept, task_concept, skills, a, b, c, d)
    
    task_c_pref = dict()
    stu_c_pref = dict()

    # generating pref order for student concepts
    for stu_c_i in range(len(aff_mat)):
        stu_c_pref[stu_c_i] = generate_pref(aff_mat, stu_c_i, True)
    # generating pref order for abstract concepts
    for task_c_i in range(len(aff_mat[0])):
        task_c_pref[task_c_i] = generate_pref(aff_mat, task_c_i, False)
    
    return task_c_pref, stu_c_pref
