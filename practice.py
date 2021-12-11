import sys

def ab(a,b):
    result=a+b
    return result

x,y=map(int,sys.stdin.readline().split())
print(ab(x,y))