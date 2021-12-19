import sys

dice=list(map(int,sys.stdin.readline().split()))
dice[3],dice[5]=dice[5],dice[3]
case=[]
min_num=dice.index(min(dice))

for i in range(min_num-2,min_num+3):
    if dice[i] == dice[min_num]:
        continue
    case.append(dice[i])


second_num=min(case)+min_num
third_num=0

third= case[case.index(min(case))+1] if case[case.index(min(case))-1] >case[case.index(min(case))+1] else case[case.index(min(case))-1] 

print(case)
print(third)