# import sys

# n,k = map(int,sys.stdin.readline().split())

# date=list(map(int,sys.stdin.readline().split()))
# result=-100

# for i in range(n-k+1):
#     temp=sum(date[i:i+k])
#     if temp>result:
#         result=temp                            

# print(result)

import sys

n,k = map(int,sys.stdin.readline().split())

date=list(map(int,sys.stdin.readline().split()))
result=[]
result.append(sum(date[:k]))

for i in range(n-k):
    result.append(result[i]-date[i]+date[i+k])
        

print(max(result))