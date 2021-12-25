n=int(input())
data=list(map(int,input().split()))
result=0
data.sort()

result=data[0]*data[-1]
    
print(result)