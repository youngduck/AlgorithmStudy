import sys

N,result=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))
cnt=0
start,end=0,1
#시간복잡도 O(n)!!
while end<=N and start<=end:
    total=sum(data[start:end])
    print(start,end)
    if total < result:
        end+=1
    elif total ==  result:
        cnt+=1
        end+=1
    else:
        start+=1
print(cnt)
