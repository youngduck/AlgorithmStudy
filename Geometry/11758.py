#Counter Clock Wise 알고리즘
#외적의값을 통해 두벡터의 시계,직선,반시계방향 위치확인가능
import sys

def CCW(x1,y1,x2,y2,x3,y3):
    external_product= (x2-x1)*(y3-y2)-(y2-y1)*(x3-x2)
    if  external_product<0:
        return -1
    elif external_product>0:
        return 1
    else:
        return 0
x1,y1=map(int,sys.stdin.readline().split())
x2,y2=map(int,sys.stdin.readline().split())
x3,y3=map(int,sys.stdin.readline().split())

print(CCW(x1,y1,x2,y2,x3,y3))


