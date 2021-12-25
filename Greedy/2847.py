n=int(input())

data=[]
cnt=0

for i in range(n):
    point=int(input())
    data.append(point)
    
for i in range(len(data)-1,0,-1):
    if data[i] <= data[i-1]:
        target=data[i]-1
        minus=data[i-1]-target
        cnt+=minus
        data[i-1]=target
        
print(cnt)