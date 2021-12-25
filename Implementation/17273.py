import sys

n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
front,back=data[:n],data[n:]
num_list=[int(sys.stdin.readline()) for i in range(m)]
choose=[0]*n
result=[]

# 0은 front 1은 back
for i in range(n):
    for num in num_list:
        if choose[i]==0:
            if front[i]<=num:
                choose[i]=1
        else:
            if back[i]<=num:
                choose[i]=0

#최종결과물
for i in range(n):
    if choose[i]==0:
        result.append(front[i])
    else:
        result.append(back[i])

print(sum(result))