import sys
n=int(sys.stdin.readline())

result=0
num=665
k=0
i=0
while i != n:
    if num == 0:
        num=k
    num+=1
    k=num
    cnt=0
    while num>0:
        if num%10 == 6:
            cnt+=1
        else:
            cnt=0
        if cnt == 3:
            i+=1
            result=k
            num=k
            break
        num=int(num/10)
              
print(result)