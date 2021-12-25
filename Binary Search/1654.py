import sys

def makeLan(arr,start):
    cnt=0
    for i in arr:
        cnt+=int(i//start)
    return cnt

k,n=map(int,sys.stdin.readline().split())

#영식이의 랜선
oh=[int(sys.stdin.readline()) for i in range(k)]


left=0
right=2**31-1
#이분탐색을만족하는 최댓값 찾기. n개이상을 만들어도 된다.
while True:
    start=int((left+right)//2)
    result=makeLan(oh,start)
    print(start,result,left,right)
    if left>=right and result>=n:
        break
    if left>=right and result!=n:
        start-=1
        break
    if result>n:
        left=start+1
    elif result<n:
        right=start-1
    else:
        left=start+1
print(start)