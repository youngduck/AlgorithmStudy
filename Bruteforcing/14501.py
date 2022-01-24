import sys
from itertools import combinations

n=int(sys.stdin.readline())

#t=기간,p=금액
schedule=[]
maxMoney=0

#데이터입력&불가능한 상담 걸러주기
for day in range(1,n+1):
    t,p=map(int,sys.stdin.readline().split())
    if day+t<=n+1:
        schedule.append([day,t,p])

for i in range(1,len(schedule)+1):
    for j in list(combinations(schedule,i)):
        d=0
        moneyCase=0
        for k in j:
            if d <k[0]:
                d=k[0]+k[1]-1
                moneyCase+=k[2]
                
        if maxMoney < moneyCase:
            maxMoney=moneyCase

print(maxMoney)