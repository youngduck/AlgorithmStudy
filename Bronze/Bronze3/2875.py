import sys
n,m,k=map(int,sys.stdin.readline().split())

usable_people=n+m-k
team_cnt=0


while usable_people>=3 and n>1 and m>0:
    usable_people=usable_people-3
    n-=2
    m-=1
    team_cnt+=1

print(team_cnt)