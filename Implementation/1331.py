#나이트 투어

import sys

c=['A','B','C','D','E','F']
r=['1','2','3','4','5','6']

board=[[i,j] for i in range(6) for j in range(6)]
result=True
visited=[]

for i in range(36):
    location=sys.stdin.readline()
    input_x=r.index(location[1])
    input_y=c.index(location[0])
    if i == 0:
        start_x,x=input_x,input_x
        start_y,y=input_y,input_y
    else:
        dis_x,dis_y=abs(input_x-x),abs(input_y-y)
        if ((dis_x+dis_y)==3)and ((dis_y*dis_x)==2):
            x=input_x
            y=input_y
            if [x,y] not in visited:
                visited.append([x,y])
        else:
            result=False
            break
    if i == 35:
    #도착점이 출발점 올 수 있는지 확인
        dis_x,dis_y=abs(start_x-x),abs(start_y-y)
        if ((dis_x+dis_y)==3)and ((dis_y*dis_x)==2):
            result=True
        else:
            result=False

if len(visited)==35 and result == True:
    print('Valid')
else:
    print('Invalid')