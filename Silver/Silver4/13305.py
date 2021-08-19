import sys
N = int(sys.stdin.readline())
dis = list(map(int,sys.stdin.readline().split()))
city = list(map(int,sys.stdin.readline().split()))
won = 0

h = city[0]
for i in range(len(dis)):
    if city[i] <= h:
        h = city[i]
    won += h*dis[i]
print(won)