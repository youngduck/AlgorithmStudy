def pp(n):
    prime=[]
    num_range=[True]*(n+1)
    num_range[0]=False
    num_range[1]=False
    for i in range(2,n+1):
        if num_range[i]:
            prime.append(i)
        for j in range(i*i,n+1,i):
            num_range[j]=False
    return prime

def cc(n):
    for j in range(int(n/2),0,-1):
        if j in prime and n-j in prime:
            print(j,n-j)
            break
prime=pp(10000)
for _ in range(int(input())):
    n=int(input())
    cc(n) 