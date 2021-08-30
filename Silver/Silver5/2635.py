import sys

n=int(sys.stdin.readline())

result=[]

for i in range(n+1):
    data=[n]
    data.append(i)
    while True:
        if data[-2]-data[-1] <0:
            break
        else:
            data.append(data[-2]-data[-1])
    if len(result)<len(data):
        result=data

print(len(result))
print(*result)