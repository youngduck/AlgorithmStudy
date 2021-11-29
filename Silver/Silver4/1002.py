import sys

data=[]
da=[]
for t in range(int(sys.stdin.readline())):
    data=list(map(int,sys.stdin.readline().split()))
    
    #큰반지름이 r1으로 설정
    if(data[2]<=data[5]):
        data[:3],data[3:]=data[3:],data[:3]
    r1,r2=data[2],data[5]
    #거리구하기
    d=((data[0]-data[3])**2+(data[1]-data[4])**2)**(1/2)
  
    #거리가 0일때
    if(d==0):
        if(r1==r2):
            print(-1)
            continue
        else:
            print(0)
            continue

    #거리가 큰원안에있을때
    if(d<r1):
        if(r1-r2>d):
            print(0)
        elif(r1-r2<d):
            print(2)
        else:
            print(1)

    #거리가 큰원밖에있을때
    elif(d>r1):
        if(r1+r2<d):
            print(0)
        elif(r1+r2>d):
            print(2)
        else:
            print(1)

    else:
        print(2)