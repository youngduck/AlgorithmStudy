import sys

n=int(sys.stdin.readline())


five=[i for i in range(n//5+1)]
two=[i for i in range(n//2+1)]
five.sort(reverse=True)
cnt=0
for i in five:
    result=n-5*i
    if result%2 == 0:
        cnt=result//2+i
        break

if cnt == 0:
    print(-1)
else:
    print(cnt)
