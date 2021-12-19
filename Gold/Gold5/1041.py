import sys

#3면이 노출되는 경우 n=2이상부터 4개
#2면이 노출되는 경우 n=2이상부터 4(2n-3)개
#1면이 노출되는 경우 n=2이상부터 (n-2)(5n-6)개

n=int(sys.stdin.readline())

dice=list(map(int,sys.stdin.readline().split()))
dice[3],dice[5]=dice[5],dice[3]
case=[]
min_num=min(dice)
min_ptr=dice.index(min(dice))
result=0

#반대편 주사위를 제거한 부분
for i in range(min_ptr-2,min_ptr+3):
    if (i%6) == min_ptr:
        continue
    case.append(dice[i%6])

second_num=min(case)+min_num
third=case[(case.index(min(case))+1)%4] if case[(case.index(min(case))-1)%4] >case[(case.index(min(case))+1)%4] else case[(case.index(min(case))-1)%4] 
third_num=third+second_num

#주사위 1개 -> 제일 큰 수 밑에 둔다.
if n ==1:
    result=sum(dice)-max(dice)
#주사위 n개 -> 3면이 노출 되는주사위 (n-2)(5n-6)개, 2면이 노출되는 주사위 4(2n-3)개
else:
    result+=4*third_num
    result+=4*(2*n-3)*second_num
    result+=(n-2)*(5*n-6)*min_num

print(result)


