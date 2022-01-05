import sys

n=int(sys.stdin.readline())
dir=[[-1,0],[0,-1],[0,1],[1,0]]
data=[list(map(int,sys.stdin.readline().split())) for i in range(n*n)]
desk_null_cnt=[[0] * n for i in range(n)]
desk=[[0] * n for i in range(n)]

for num in data:
    student=num[0]
    love_list=num[1:]
    max_null_cnt=-1
    max_love_cnt=-1
    for x in range(n-1,-1,-1):
        for y in range(n-1,-1,-1):
            null_cnt=0
            love_cnt=0
            for r,c in dir:
                if x+r <0 or x+r>n-1 or c+y<0 or c+y>n-1:
                    continue
                if desk[x+r][c+y] == 0:
                    null_cnt+=1
                if desk[x+r][c+y] in love_list:
                    love_cnt+=1
            if(max_null_cnt)
            