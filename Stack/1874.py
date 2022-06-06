import sys

n=int(sys.stdin.readline())

data=[0]*n

for i in range(n):
    data[i]=int(sys.stdin.readline())

cur=1
idx=0
make=True
stack=[]
result=''

for i in data:
    if cur<=i:
        for j in range(cur,i+1):
            stack.append(j)
            result+='+'
        else:
            cur=j+1
    if i == stack[-1]:
        stack.pop()
        result+='-'
    else:
        make=False
        break

if make:
    for i in result:
        print(i)
else:
    print("NO")