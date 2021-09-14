import heapq

data=[[1,2],[3,4],[5,6],[7,8]]
new=list(filter(lambda x:x[0]>3,data))

# heapq.heappush(data,11)
# heapq.heappush(data,5)
# heapq.heappush(data,4)
# heapq.heappush(data,10)


print(data)
print(new)
print(max(lambda x:x[0],new))