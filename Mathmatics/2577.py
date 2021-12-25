a=int(input())
b=int(input())
c=int(input())
d=str(a*b*c) #d=12311514
n=0
for j in range(10):
    for i in d:
        if int(i) == j:
            n+=1
    print(n)
    n=0