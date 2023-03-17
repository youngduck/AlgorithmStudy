import sys


data=[]
for i in range(int(sys.stdin.readline())):
    age,name=sys.stdin.readline().split()
    data.append([int(age),name])

data=sorted(data,key=lambda x:x[0])


for i in data:
    print(*i)