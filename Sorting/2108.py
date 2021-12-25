import sys
N=int(sys.stdin.readline())
num=[]
for i in range(N):
    n=int(sys.stdin.readline())
    num.append(n)
def count(num):
    if len(num) == 1:
        return num[0]
    d={}
    for i in num:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d=sorted(d.items(),key=(lambda x:x[1]),reverse=True)
    if d[0][1] == d[1][1] :
        return d[1][0]
    else :
        return d[0][0]
num.sort()
center=num[int((N-1)/2)]

print(round(sum(num)/N))#1번째답
print(center)#2번째답
print(count(num))
print(max(num)-min(num))