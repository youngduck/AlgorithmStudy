import sys

#초깃값 설정
cityNum=int(sys.stdin.readline())
city=list(map(int,sys.stdin.readline().split()))
budget=int(sys.stdin.readline())
budgetList=[]

def sumMoney(city,mid):
    money=0
    for i in city:
        if i<mid:
            money+=i
        else:
            money+=mid
    return money

#첫번째 조건.
if sum(city) <budget:
    result=max(city)

#두번째 조건.
else:
    left,right=0,max(city)
    while left<=right:
        mid=int((left+right)/2)
        #람다함수 쓰려했으나 else의 경우를 반환하지못하므로 pass
        money=sumMoney(city,mid)
        if money <=budget:
            budgetList.append(mid)
            left=mid+1
        else:
            right=mid-1
    result=max(budgetList)
        
print(result)