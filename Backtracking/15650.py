#combination활용 풀이

# from itertools import combinations
# import sys

# n,m=map(int,sys.stdin.readline().split())
# data=list(range(1,n+1))
# for i in list(combinations(data,m)):
#     print(*i)

import sys

n,m=map(int,sys.stdin.readline().split())

number=list(range(1,n+1))
number_visit=[False]*(len(number)+1)
data=[0]*m

def back(n,m,index):
    if index==m:
        if m ==1:
            print(*data)
            return
        else:
            sortData=sorted(data)
            if sortData==data:
                print(*data)
            return

    for i in number:
        if number_visit[i]==False:
            data[index]=i
            number_visit[i]=True
            back(n,m,index+1)
            number_visit[i]=False

back(n,m,0)