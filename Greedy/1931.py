import sys
N=int(sys.stdin.readline())

data=[list(map(int,sys.stdin.readline().split())) for i in range(N)]

data=sorted(data,key=lambda x:(x[1],x[0]))

time=data[0][1]
cnt=1

for i in data[1:]:
    if time <= i[0]:
        time = i[1]
        cnt+=1
print(cnt)