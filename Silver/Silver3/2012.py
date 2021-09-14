import sys

n=int(sys.stdin.readline())
#무조건 사람들은 1등부터 n등까지 한명씩있음.
data=[int(sys.stdin.readline()) for i in range(n)]
data.sort()
result=0

for i in range(n):
    dis=abs(data[i]-(i+1))
    result+=dis


print(result)