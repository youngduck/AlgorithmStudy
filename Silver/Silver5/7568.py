N=int(input())
data=[]

for i in range(N):
    weight,height=map(int,input().split())
    data.append((weight,height))
    
for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank,end=' ')