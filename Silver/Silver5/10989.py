import sys
N=int(sys.stdin.readline())
num_range=[0]*10001
for i in range(N):
    a=int(sys.stdin.readline())
    num_range[a]+=1
for j in range(len(num_range)):
    if num_range[j] != 0:
        for k in range(num_range[j]):
            print(j)