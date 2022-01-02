from itertools import combinations
import sys

L,C=map(int,sys.stdin.readline().split())

vowel=['a','e','i','o','u']
password_c=[]
password_v=[]

data=list(sys.stdin.readline().split())


#자음 모음 분리
for i in data:
    if i in vowel:
        password_v.append(i)
    else:
        password_c.append(i)

result=[]

for i in range(1,len(password_v)+1):
    if((len(password_c)+1)>=1 and (L-i)>=2):
        for j in list(combinations(password_v,i)):
            for k in list(combinations(password_c,L-i)):
                temp=list(j)+list(k)
                temp.sort()
                result.append(temp)
result.sort()

for i in result:
    print(*i,sep='')
    