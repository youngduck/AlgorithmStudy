import sys

data=[]

for i in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    if(num==0):
        data.pop()
    else:
        data.append(num)
print(sum(data))