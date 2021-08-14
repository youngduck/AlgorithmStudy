N=int(input())

data=[N]*N
rating=list(map(int,input().split()))
for cm in range(1,N+1):
    cnt=0
    rate=rating[cm-1]
    for i in range(N):
        if cm < data[i]:
            cnt+=1
            if cnt>rate:
                data[i]=cm
                break
                
for i in data:
    print(i,end=' ')