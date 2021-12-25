import sys

#입력받기
r,c=map(int,sys.stdin.readline().split())
a,b=map(int,sys.stdin.readline().split())
case1=[]
case2=[]

#case1 만들기
sw=0
for i in range(c):
    if sw == 0:
        case1+='X'*b
        sw=1
    else:
        case1+='.'*b
        sw=0

#case2 만들기
sw=1
for i in range(c):
    if sw == 0:
        case2+='X'*b
        sw=1
    else:
        case2+='.'*b
        sw=0
#번갈아가며 출력하기
sw=0
for i in range(r):
    if sw == 0 :
        for j in range(a):
            print(*case1,sep='')
        sw=1
    else:
        for j in range(a):
            print(*case2,sep='')
        sw=0
