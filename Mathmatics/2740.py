# import numpy
import sys

#행렬계산 numpy 이용!
#numpy.dot()

N,M=map(int,sys.stdin.readline().split())
data_a=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
M,K=map(int,sys.stdin.readline().split())
data_b=[list(map(int,sys.stdin.readline().split())) for i in range(M)]
data_c=[[0]*K for i in range(N)]


for n in range(N):
    for k in range(K):
        for m in range(M):
            data_c[n][k]+=data_a[n][m]*data_b[m][k]

for i in data_c:
    print(*i)
