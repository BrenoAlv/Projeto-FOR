A=[]
lis=10
lis2=10
for i in range(10):
    A.append(int(input('digite {} valores'.format(lis))))
    lis=lis-1
B=[]
for i in range(10):
    B.append(int(input('digite mais {} valores'.format(lis2))))
    lis2=lis2-1
C=[]
for elemA, elemB in zip(A, B):
    C.append(elemA + elemB)
print(C)