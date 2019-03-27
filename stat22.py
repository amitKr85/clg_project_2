# Python3 Program to check if two
# given matrices are identical

N = 10
comb = [[]]

# This function returns 1
# if A[][] and B[][] are identical
# otherwise returns 0
def areSame(A, B):
    for i in range(N):
        for j in range(N):
            if (A[i][j] != B[i][j]):
                return 0
    return 1


# driver code
A = [[1, 1, 1, 1, 0, 0, 1, 0],
     [1, 1, 0, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 1, 1, 0, 0],
     [0, 1, 1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 1, 0]]

B= [[1, 1, 1, 1, 0, 0, 0, 0 ],
     [1, 1, 0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 1, 0]]

def pairs(A, B):
    for i in range(N):
        for j in range(N):
            if (A[i][j] != B[i][j]):
                return 0
    return 1

def findor(arr,A):
    arr1= []
    for i in range(len(A)):
        arr1.append(arr[i] or A[i])
       # print(arr1)
    return arr1
def givecombinterm(grp,A):
    #print(grp)
    arr2= []
    arr= []
    for i in range(len(grp)):
        if i== 0:
            arr=A[grp[i]-1]
            print(arr)
        else:
            #arr = arr or A[grp[i]-1]
            arr = findor(arr,A[grp[i]-1])
            #print(arr)

    arr2.append(arr)
    #print(arr2
    return arr2

def sumcommonskills(grp,B):
    sum=0
    for i in range(len(B)):
        if grp[i]and B[i]== 1:
            sum=sum+1
    return sum



a1= []

M=4
group = [M]
grp1 = [[1,2,4],
 [3,5,6],
[7,4],
 [6,8]]


for i in range(len(grp1)):
    group.append(givecombinterm(grp1[i],A))
   # print("----------------")
#for i in range(0,len(group)):
    #print(group[i],end = ' \n')
#print("-----------------")

print("group",group)

for i in range(len(B)):
    for j in range(len(B)):
        a2=[]
        for k in range(M):
            sum = 0
            for l in range(len(B)):
                if group[k][l] and B[i][l] == 1:
                    sum = sum + 1
            a2[k]= sum
    a1.append(a2)
for i in range(0,len(a1)):
    print(a1[i],end = ' \n')
#print(absskaasillgrptable(group,B))
#print(group[1])
