import sys

data=[list(map(float,sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))]
data=sorted(data,key=lambda x:(x[0],x[1]))
data.append([data[0][0],data[0][1]])
print(data)
num1,num2=0,0

for i in range(len(data)-1):
    num1+=data[i][0]*data[i+1][1]
    num2+=data[i][1]*data[i+1][0]
    print(num1,num2)

print("%.1f"%((num1-num2)/2))