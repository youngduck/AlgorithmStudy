m,n=map(int,input().split())

num_range=[True]*(n+1)

num_range[0]=False
num_range[1]=False

for i in range(2,n+1):
    if num_range[i] and i>=m:
        print(i)
    for j in range(i*2,n+1,i):
        num_range[j]=False