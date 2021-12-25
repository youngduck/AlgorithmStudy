num=int(input())
n=0
k=num
while True:
    a=k//10
    b=k%10
    c=a+b
    a=(b*10)+(c%10)
    n+=1
    if num==a:
        print(n)
        break
    else:
        k=a