import sys

n,m=map(int,sys.stdin.readline().split())

d={}

for i in range(n):
    site,password=sys.stdin.readline().split()
    d[site]=password

for i in range(m):
    find=sys.stdin.readline().rstrip()
    print(d[find])
