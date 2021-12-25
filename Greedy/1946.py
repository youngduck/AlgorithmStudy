import sys
T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    data=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
    data=sorted(data,key=(lambda x:x[0]))   
    cnt=1
    dafault=data[0][1]
    
    for i in range(1,N):
        if dafault>data[i][1]:
            dafault=data[i][1]
            cnt+=1
    print(cnt)