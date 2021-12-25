N=int(input())
A=[]
for i in range(N):
    a=int(input())
    A.append(a)
A.sort()
for i in A:
    print(i)