#한수의 갯수 -> 100보다작은수 전부 한수,
def hansu(N):
    cnt=0
    for i in range(1,N+1):
        if i <100:
            cnt +=1
        if 100<=i<1000:
            num=str(i)                        
            for k in range(len(num)-2):
                if int(num[k+2])-int(num[k+1])==int(num[k+1])-int(num[k]):
                    cnt+=1
        if i==1000:
            cnt=144
    return cnt

N=int(input())
print(hansu(N))