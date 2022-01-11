import sys

#초깃값 세팅
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())

#집중국이 더많을경우 모든 센서에 집중국을 세울수 있으므로 거리 0
if n<=k:
    print(0)

#각 센서들을 정렬후 센서간 거리를 넣어준다.
else:
    road=list(map(int,sys.stdin.readline().split()))
    road.sort()
    dis=[0]*(len(road)-1)

    for i in range(len(dis)):
        dis[i]=road[i+1]-road[i]
    dis.sort()

#가장 먼 센서간거리를 소거하는 방법으로 집중국을 배치.
    for i in range(k-1):
        dis.pop()
    print(sum(dis))