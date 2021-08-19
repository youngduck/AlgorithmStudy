A,B,V=map(int,input().split(' '))
import math
if A>=V:
    day=1
else:
    day=(math.ceil((V-A)/(A-B)))+1
print(int(day))