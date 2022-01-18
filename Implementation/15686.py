import sys
from itertools import combinations

n,m=map(int,sys.stdin.readline().split())
home_list=[]
chicken_list=[]

#집,치킨집 좌표찾기.
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    
    home_c=list(filter(lambda x:line[x]==1,range(len(line))))
    home_r=[i]*len(home_c)
    home=list(zip(home_r,home_c))
    home_list.extend(home)

    chicken_c=list(filter(lambda x:line[x]==2,range(len(line))))
    chicken_r=[i]*len(chicken_c)
    chicken=list(zip(chicken_r,chicken_c))
    chicken_list.extend(chicken)

result=100000
dis_list=[]

for i in list(combinations(chicken_list,m)):
    chicken_dis=0    
    for j in home_list:
        for k in i:
            dis=abs(k[0]-j[0])+abs(k[1]-j[1])
            dis_list.append(dis)
        chicken_dis+=min(dis_list)
        dis_list=[]

    if result>chicken_dis:
        result=chicken_dis
print(result)