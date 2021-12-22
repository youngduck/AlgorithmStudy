import sys
import heapq

data=[]
result=[]

#2중 for문으로 만들었더니 시간초과나옴
#heapq를 이용하여 시간단축.

for n in range(int(sys.stdin.readline())):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort()
heapq.heappush(result,data[0][1])
print(data)
for i in range(1,len(data)):
    #result[0]을쓰는 이유 
    #가장 빨리끝나는시간과 가장 일찍 시작하는시간 매칭가능
    #그래서 2중for문을 안써도됨
    if result[0] <= data[i][0]:
        heapq.heappop(result)
        heapq.heappush(result,data[i][1])
    else:
        heapq.heappush(result,data[i][1])

print(len(result))
