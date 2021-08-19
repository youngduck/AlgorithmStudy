data=[list(map(int,input().split())) for _ in range(int(input()))]

data=sorted(data,key=lambda x:(x[0],x[1]))

for i in data:
    print("%d %d" %(i[0],i[1]))