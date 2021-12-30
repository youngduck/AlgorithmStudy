import sys

data=[]
for i in range(int(sys.stdin.readline())):
    data.append(int(sys.stdin.readline()))

if(data.count(0)>data.count(1)):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")