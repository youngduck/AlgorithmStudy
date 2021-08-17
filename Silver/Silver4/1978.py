import sys
N=int(input())
a=list(map(int,input().split()))
cnt=0
for i in a:
    b=[]
    for j in range(1,i+1):
        if i%j==0:
            b.append(j)
    if len(b)==2:
        cnt+=1
print(cnt)