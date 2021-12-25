import sys

n,m=map(int,sys.stdin.readline().split())
map=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
spot=[]
line=0

for i in map:
    line+=1
    try:
        one=i.index(1)
        spot.append([line,one+1])
    except:
        continue
    

x=abs(spot[0][0]-spot[1][0])
y=abs(spot[0][1]-spot[1][1])

print(x+y)