N,L=map(int,input().split())

data=list(map(int,input().split()))
data.sort()

for i in data:
    for j in range(L-1):
        i+=1
        if i in data:
            data.remove(i)
            
            
print(len(data))