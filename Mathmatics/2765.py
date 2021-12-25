import sys
PI=3.1415927
n=1
while True:
    
    #예제 입력 지름(inch), 회전수(정수), 시간(초단위 실수)
    diameter,cnt,second=map(float,sys.stdin.readline().split())
    diameter=diameter/12/5280
    hour=second/3600
    
    if cnt ==0:
        break
    else:
        #계산과정
        distance=round(PI*diameter*cnt,2)
        MPH=round(PI*diameter*cnt/hour,2)
        #출력 Trip #N : 총 거리(miles) 평균속도(miles per hour)
        print("Trip #%d : %0.2f %0.2f"  %(n,distance,MPH))
        n+=1
        



        



