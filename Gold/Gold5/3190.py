import sys

#입력값,초깃값
n=int(sys.stdin.readline())
stack=[[1,1]]
start=[1,1]
dir=[[0,1],[1,0],[0,-1],[-1,0]]
dir_type=0
time=0
trash=[0,0]

#사과 조건 입력
apple_cnt=int(sys.stdin.readline())
apple_zone=[]

for i in range(apple_cnt):
    row,column=map(int,sys.stdin.readline().split())
    apple_zone.append([row,column])

#방향 조건 입력
turn_cnt=int(sys.stdin.readline())
turn_time=[]
turn_dir=[]

for i in range(turn_cnt):
    t,direction=sys.stdin.readline().split()
    turn_time.append(int(t))
    turn_dir.append(direction)


#실행 되는 부분
while True:
    
    time+=1    
    start[0]+=dir[dir_type][0]
    start[1]+=dir[dir_type][1]
    snake=[start[0],start[1]]
    stack.append(snake)

    #탈출 조건 설정
    if (start[0] > n or start[0]<=0) or (start[1]>n or start[1]<=0):
        break
    if snake in stack[:-1]:
        break
        
    #사과 조건 설정
    if start in apple_zone:
        apple_zone.pop(apple_zone.index(start))
    else:  
        trash=stack.pop(0)
        
    #dir 조건 설정
    if time in turn_time:
        if turn_dir[turn_time.index(time)]=='D':
            dir_type=(dir_type+1)%4
        else:
            dir_type=(dir_type-1)%4

print(time)