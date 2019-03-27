import numpy as np
import pandas as pd

tech_csv_path = "test_files/temp_tech_formal_context.csv"
stu_csv_path = "test_files/temp_student_formal_context.csv"

stu_skill_mat = np.array(pd.read_csv(stu_csv_path).replace([np.nan,'X'],[0, 1]).iloc[:,1:].values,dtype='int')
proj_skill_mat = np.array(pd.read_csv(tech_csv_path).replace([np.nan,'X'],[0,1]).iloc[:,1:].values,dtype='int')

stu_dist = np.zeros((stu_skill_mat.shape[0],stu_skill_mat.shape[0]))

for i in range(stu_skill_mat.shape[0]):
    for j in range(stu_skill_mat.shape[0]):
        if i != j:
            stu_dist[i][j] = stu_dist[j][i] = np.sum(np.bitwise_xor(stu_skill_mat[i,:],stu_skill_mat[j,:]))

print(stu_dist)

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

stu_Z = hierarchy.linkage(stu_dist, 'single')
print(stu_Z)
plt.figure()
plt.xlabel('students')
dn = hierarchy.dendrogram(stu_Z)


# /////////////////////////////////////////////

proj_dist = np.zeros((proj_skill_mat.shape[0],proj_skill_mat.shape[0]))

for i in range(proj_skill_mat.shape[0]):
    for j in range(proj_skill_mat.shape[0]):
        if i != j:
            proj_dist[i][j] = proj_dist[j][i] = np.sum(np.bitwise_xor(proj_skill_mat[i,:],proj_skill_mat[j,:]))

print(proj_dist)
proj_Z = hierarchy.linkage(proj_dist, 'single')
print(proj_Z)
plt.figure()
plt.xlabel('projects')
dn = hierarchy.dendrogram(proj_Z)