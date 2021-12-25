n=int(input())

for i in range(n):    
    s=0
    k=0
    a=input()
    for j in a: #a='oooxoxoxxo'
        if j=='O':
            s+=1
            k+=s
        else:
            s=0
    print(k)