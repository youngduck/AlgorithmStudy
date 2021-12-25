import sys

n,q=map(int,sys.stdin.readline().split())

song=list(map(int,sys.stdin.readline().split()))

for i in range(q):
    result=0
    start,end=map(int,sys.stdin.readline().split())
    for j in range(start,end):
        result+=abs(song[j-1]-song[j])
    print(result)