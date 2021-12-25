#출발점,도착점이 원안에 존재하는 경우를 따지면 된다.
#두점이 동시 같은원안에 존재할경우에는 cnt변화 x
#두점중 한점만 원안에 존재할 시 cnt++
import sys
for t in range(int(sys.stdin.readline())):
    cnt=0
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for circle in range(int(sys.stdin.readline())):
        #원의 좌표
        cX,cY,r=map(int,sys.stdin.readline().split())
        
        #원의중심과 출발점 도착점 거리비교
        d1=(cX-x1)**2+(cY-y1)**2
        d2=(cX-x2)**2+(cY-y2)**2
        
        #출발점은 원안에있고 도착점은 원밖에 있는경우
        if d1<r**2:
            if d2>r**2:
                cnt+=1
        #출발점은 원안에있고 도착점은 원밖에 있는경우
        if d2<r**2:
            if d1>r**2:
                cnt+=1
    print(cnt)