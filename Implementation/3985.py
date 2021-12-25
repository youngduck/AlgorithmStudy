import sys

#롤 케이크 길이
L=int(sys.stdin.readline())
#방척객 수
N=int(sys.stdin.readline())

cake=[False]*(L+1)

paper=[]
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

expect=[]
take=[]
num=1
for i,j in paper:
    cnt=0
    for k in range(i,j+1):
        if cake[k] == False:
            cake[k]=True
            cnt+=1
    expect.append([num,j-i])
    take.append([num,cnt])
    num+=1

expect=sorted(expect,key=lambda x:(x[1]),reverse=True)
take=sorted(take,key = lambda x:(x[1]),reverse=True)
   
print(expect[0][0])
print(take[0][0])

