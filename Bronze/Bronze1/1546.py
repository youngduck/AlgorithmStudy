n=int(input())
a=list(map(int,input().split()))
#최댓값고르기(M) ->모든점수 점수/m*100 -> 평균내기
M=max(a)
new_a=[]
sum=0
for i in a:
    b=i/M*100
    new_a.append(b)
for i in new_a:
    sum+=i
avr=sum/(len(new_a))
print(avr)