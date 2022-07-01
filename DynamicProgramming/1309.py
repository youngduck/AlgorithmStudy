import sys
#한 행을 기준으로 왼쪽(ox) 오른쪽(xo) 없음(xx)가 존재할 수 있다.
#한 행씩 각열의 경우(왼쪽,오른쪽,없음)에 따라 누적하여 경우의 수를 더해준다.
#점화식으로 해결 가능.

import sys

N=int(sys.stdin.readline())


data=[[0]*3 for _ in range(N+1)]

data[1][0],data[1][1],data[1][2]=1,1,1



#반목문실행마다 9901로 나누어주는 이유 -> 너무 큰숫자를 사용하여 메모리가 과다하게 사용되는걸 방지
for i in range(2,N+1):
    #왼쪽(ox)일때 전행이 오른쪽,없음일때의 경우의수를 더할 수 있음.
    data[i][0]=(data[i-1][1]+data[i-1][2])%9901
    #오른쪽(xo)일때 전행이 왼쪽,없음일때의 경우의수를 더할 수 있음.
    data[i][1]=(data[i-1][0]+data[i-1][2])%9901
    #없음(xx)일때 전행이 왼쪽,오른쪽 없음 모든경우의수를 더할 수 있음.
    data[i][2]=(data[i-1][0]+data[i-1][1]+data[i-1][2])%9901
    
result=(data[N][0]+data[N][1]+data[N][2])%9901
print(result)