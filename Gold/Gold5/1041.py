import sys

n=int(sys.stdin.readline())

dice=list(map(int,sys.stdin.readline().split()))
dice[3],dice[5]=dice[5],dice[3]
case=[]
min_num=dice.index(min(dice))

#반대편 주사위를 제거한 부분
for i in range(min_num-2,min_num+3):
    if dice[i] == dice[min_num]:
        continue
    case.append(dice[i])

second_num=min(case)+min_num
third_num=case[case.index(min(case))+1] if case[case.index(min(case))-1] >case[case.index(min(case))+1] else case[case.index(min(case))-1] 

#3면이 노출되는 경우
#2면이 노출되는 경우

second_num=


#주사위 1개 -> 제일 큰 수 밑에 둔다.
if n ==1:
    print(sum(dice)-max(dice))
#주사위 2개 -> 3면이 노출 되는주사위 4개, 2면이 노출되는 주사위 4개
elif n == 2:


