from generate_concept_matrix import *
from get_preferences import *
from extended_sma import *


def get_participation(concept_pairs, tasc, tesc, abstracts, students, skills):
    project_part = dict()
    student_part = dict()

    for abst_con_i, stu_cons_i in concept_pairs:
        tasc_row = tasc[abst_con_i]
        tesc_row = tesc[stu_cons_i]

        proj_list = []
        stu_list = []

        for i in range(len(tasc_row)):
            if tasc_row[i] == 1:
                if i < len(skills):
                    print(skills[i], end=" | ")
                else:
                    print(abstracts[i - len(skills)], end=" | ")
                    proj_list.append(i - len(skills))
        print(" > ", end="")
        for i in range(len(tesc_row)):
            if tesc_row[i] == 1:
                if i < len(skills):
                    print(skills[i], end=" | ")
                else:
                    print(students[i - len(skills)], end=" | ")
                    stu_list.append(i - len(skills))

        for proj in proj_list:
            for stu in stu_list:
                if proj in project_part:
                    project_part[proj].add(stu)
                else:
                    project_part[proj] = {stu}

                if stu in student_part:
                    student_part[stu].add(proj)
                else:
                    student_part[stu] = {proj}
        print()

    return project_part, student_part


def main():
    # concept matrix, row, column
    # for projects
    tasc, abstracts, skills = generate_concept_matrix("test_files/temp_tech_formal_context.csv")
    print("abstract concept matrix")
    for row in tasc:
        print(row)
    # for students
    tesc, students, skills = generate_concept_matrix("test_files/temp_student_formal_context.csv", skills)
    print("student concept matrix")
    for row in tesc:
        print(row)

    print("---------------------------------------------------------------------------")
    # get dictionary key as project/student index value as list of preference
    task_c_pref, stu_c_pref = get_preferences(tesc, tasc, skills)
    print("student preferences")
    for k, v in stu_c_pref.items():
        print(k, v)

    print("project preferences")
    for k, v in task_c_pref.items():
        print(k, v)

    print("---------------------------------------------------------------------------")
    print("applying sma")
    concept_pairs = extended_sma(task_c_pref, stu_c_pref)
    print("task_concept-student_concept pairs")
    print(concept_pairs)

    project_part, student_part = get_participation(concept_pairs, tasc, tesc, abstracts, students, skills)
    print("---------------------------------------------------------------------------")
    print("project part ....")
    for proj, stus in project_part.items():
        print(abstracts[proj], "(", len(stus), ")", ">", end="{")
        for s in stus:
            print(students[s], end=",")
        print("}")

    print("---------------------------------------------------------------------------")
    print("student part ....")
    for stus, proj in student_part.items():
        print(students[stus], "(", len(proj), ")", ">", end="{")
        for p in proj:
            print(abstracts[p], end=",")
        print("}")




if __name__ == "__main__":
    main()
