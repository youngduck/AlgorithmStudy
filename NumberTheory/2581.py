M=int(input())
N=int(input())
pnum=[] #소수
for i in range(M,N+1):
    div=[] #약수갯수
    for j in range(1,i+1):
        if i%j==0:
            div.append(j)
    if len(div) == 2:
        pnum.append(i)
if len(pnum) == 0:
    print(-1)
else:
    print(sum(pnum))
    print(min(pnum))    
