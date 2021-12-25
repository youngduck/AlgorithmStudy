import sys
N=int(sys.stdin.readline())
weight=list(map(int,sys.stdin.readline().split()))

weight.sort()
result=0
for i in weight:
    if result+1 >= i:
        result+=i
    else:
        break
print(result+1)