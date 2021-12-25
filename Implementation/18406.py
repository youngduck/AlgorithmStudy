import sys
num=sys.stdin.readline().rstrip()
result1=0
result2=0

half=int(len(num)//2)
for i in range(len(num)):
    if half>i:
        result1+=int(num[i])
    else:
        result2+=int(num[i])
if result1 == result2:
    print("LUCKY")
else:
    print("READY")