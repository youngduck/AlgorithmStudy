import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

target_list=list(map(int,sys.stdin.readline().split()))
people=[0]*N

for m in range(M):
    expect=list(map(int,sys.stdin.readline().split()))
    target=target_list[m]
    for n in range(N):
        if expect[n] == target:
            people[n]+=1
        else:
            people[target-1]+=1
            
for i in people:
    print(i)

