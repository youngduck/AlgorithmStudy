n,m=map(int,input().split())

arr=[]
visit=[]
for i in range(0,n):
    visit.append(False)

for i in range(0,m):
    arr.append('')

def dfs(n,m,d):
    if d==m:
        for i in range(0,m):
            print(str(arr[i])+' 'if i !=len(arr) else'',end='')
        print()
        return
    for i in range(0,n):
        if visit[i] ==False:
            visit[i] = True
            arr[d]=i+1
            dfs(n,m,d+1)
            visit[i] = False

dfs(n,m,0)
