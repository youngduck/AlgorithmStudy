import sys

num = ['zero','one','two','three','four','five','six','seven','eight','nine']

n,m = map(int,sys.stdin.readline().split())
data=[]

for i in range(n,m+1):
    if i >=10:
        newNum=num[i//10]+num[i%10]
    else:
        newNum=num[i%10]
    data.append([newNum,i])

result = sorted(data,key=lambda x:x[0])


# 한줄에 10개씩 출력
count = 0
for i in result:
    if count == 9:
        print(i[1])
        count=0
    else:
        print(i[1],end=' ')
        count+=1