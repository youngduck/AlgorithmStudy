import sys
B=['B','W','B','W','B','W','B','W']
W=['W','B','W','B','W','B','W','B']

start_B=[]
start_W=[]

for i in range(4):
    start_B.append(B)
    start_B.append(W)
    start_W.append(W)
    start_W.append(B)
    
y,x=map(int,sys.stdin.readline().split())

Board=[[] for _ in range(y)]

for i in range(y):
    line = sys.stdin.readline()
    for j in range(x):
        Board[i].append(line[j])
result=64

for i in range(y-7):
    for j in range(x-7):
        count1=0
        count2=0
        for k in range(8):
            for l in range(8):
                if Board[i+k][j+l] != start_B[k][l]:
                    count1+=1
                if Board[i+k][j+l] != start_W[k][l]:
                    count2+=1
        result=min(result,count1,count2)
print(result)