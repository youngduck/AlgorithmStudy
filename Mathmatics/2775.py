T=int(input())
for i in range(T):
    k=int(input()) #k=층
    n=int(input()) #n=호수
    a=[]
    result=0
    for i in range(n):
        a.append(i+1)
    if k == 0:
        print(a[n-1])
    else:
        for _ in range(k):
            c=[]
            for i in range(len(a)):
                b=a[:i+1]
                result=sum(b)
                c.append(result)
            a=c
        print(a[n-1])