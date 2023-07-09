import sys

data=[int(sys.stdin.readline()) for i in range(9)]
find = False

for i in range(9):
    for j in range(i+1,9):
        sum_height=sum(data)-data[i]-data[j]
        n1=data[i]
        n2=data[j]
        if sum_height==100:
            data.remove(n1)
            data.remove(n2)
            find = True
            break
    if find:
        break

data.sort()
for i in data:
    print(i)