import sys
n,m=map(int,sys.stdin.readline().split())
data=[]
tree=list(map(int,sys.stdin.readline().split()))
low=0
top=max(tree)
while low<=top:
    
    h=(top+low)//2
    take=sum(i-h if i>h else 0 for i in tree)
    if take>=m:
        low=h+1
        data.append(h)
    elif take<m:
        top=h-1

print(max(data))