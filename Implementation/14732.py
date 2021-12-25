import sys

n=int(sys.stdin.readline())
data=[[0]*500 for i in range(500)]
cnt=0
for i in range(n):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            if data[j][k] == 0:
                data[j][k]=1
                cnt+=1
                
            
print(cnt)
