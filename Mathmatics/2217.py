N=int(input())

lope=[]
weight=[]

for i in range(N):
    lope.append(int(input()))
lope.sort()

for i in range(N):
    weight.append(lope[i]*(N-i))
    
print(max(weight))