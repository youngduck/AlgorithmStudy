import sys

n,m=map(int,sys.stdin.readline().split())

def dfs(x,y):
    #주어진 범위를 벗어나느 ㄴ경우 즉시종료
    if(x<=-1 or x>=n or y<=-1 or y>=m):
        return False
    #현재 노드를 아직 방문 x
    if graph[x][y]==0:
        graph[x][y]=1
        #상하좌우 모두재귀적호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#2차원 리스트의 맵 정보 입력 받기

graph=[list(map(int,sys.stdin.readline().rstrip())) for i in range(n)]

#모든 노드에 대하여 음료수 채우기
result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result +=1

print(result)