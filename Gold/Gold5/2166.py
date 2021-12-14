#신발끈공식 사용

import sys

data=[list(map(float,sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))]
data.append([data[0][0],data[0][1]])
num1,num2=0,0

for i in range(len(data)-1):
    num1+=data[i][0]*data[i+1][1]
    num2+=data[i][1]*data[i+1][0]

print("%.1f"%(abs((num1-num2)/2)))