N=int(input())
result=[]

for i in range(N):
    num=str(i)
    sum_num=0
    for j in range(len(num)): #각자릿수합
        sum_num+=int(num[j])
    if i +sum_num == N:
        result.append(i)
        
if len(result)==0:
    print(0)
else:
    print(min(result))