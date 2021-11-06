import sys

a=list(map(int,sys.stdin.readline().split()))
c=list(map(int,sys.stdin.readline().split()))

b=[c[0]-a[2],int(c[1]/a[1]),c[2]-a[0]]

print(*b)