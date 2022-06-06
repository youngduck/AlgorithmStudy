import sys

n=int(sys.stdin.readline())


data=[sys.stdin.readline().rstrip() for i in range(n)]
data=list(set(data))

for i in sorted(data,key=lambda x:(len(x),x)):
    print(i)

