from re import I
from struct import pack
import sys

#n:기타줄 개수  m:브랜드
n,m=map(int,sys.stdin.readline().split())
package_cheap=1001
indivisual_cheap=1001
result=100000

#패키지최솟값,낱개최솟값 추출
for _ in range(m):
    p,i=map(int,sys.stdin.readline().split())
    if p<package_cheap:
        package_cheap=p
    if i<indivisual_cheap:
        indivisual_cheap=i

#추출한 최솟값들로 패키지기준 내림차순 전수검사.
for i in range(n//6+1,-1,-1):
    #몫의 변화에 따른 초깃값
    money=0
    cnt=n
    #몫,나머지에 따른 계산
    cnt-=i*6
    if cnt>0:
        money+=cnt*indivisual_cheap
    money+=package_cheap*i
    
    #최솟값
    if money<result:
        result=money

print(result)