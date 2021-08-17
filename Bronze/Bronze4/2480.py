data=list(map(int,input().split()))

s1=set(data)
data.sort()

if len(s1) == 1:
    print(data[0]*1000+10000)
if len(s1) == 2:
    print(data[1]*100+1000)
if len(s1) == 3:
    print(data[2]*100)