import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
sameRange=1

for i in range(int(sys.stdin.readline())):
    gender,index=map(int,sys.stdin.readline().split())
    if gender==1:
        for i in range(index-1,n,index):
            data[i]=1-data[i]
    else:
        data[index-1]=1-data[index-1]
        for i in range(1,int(n/2)):
            if(index-1-i<0 or index-1+i>=n):
                break
            if data[index-1-i] == data[index-1+i]:
                data[index-1-i]=1-data[index-1-i]
                data[index-1+i]=1-data[index-1+i]
            else:
                break
cnt=1
for i in data:
    print(i,end=' ')
    if(cnt%20==0):
        print()
    cnt+=1
    
