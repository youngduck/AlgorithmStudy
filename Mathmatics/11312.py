import sys

for t in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    print(int((a/b)**2))    