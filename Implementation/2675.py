T=int(input())
for i in range(T):
    R,S=input().split(' ')
    R=int(R)
    
    a=[]
    for i in S:
        for j in range(R):
            a.append(i)
    print(''.join(a))