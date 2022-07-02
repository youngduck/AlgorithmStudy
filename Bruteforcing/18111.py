import sys
from collections import Counter
#가장낮은시간 중 땅의높이가 가장높은것. 개수제한도있음
#빈칸만큼 채우느냐? 삭제하느냐?
N,M,B=map(int,sys.stdin.readline().split())

ground=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
count=Counter({})
for i in range(N):
    count += Counter(ground[i])

result=[]

for height in range(min(count.keys()),max(count.keys())+1):
    time=0
    block_cnt=B
    for key,value in  dict(count).items():
        use_block=abs(height-key)*value
        
        if height>key:#건설작업 1초
            time+=use_block*1
            block_cnt-=use_block
        
        elif height<key:#제거작업 2초
            time+=use_block*2
            block_cnt+=use_block

    if block_cnt>=0:
        result.append([time,height,block_cnt])

result=sorted(result,key=lambda x:(x[0],-x[1]))

print(result[0][0],result[0][1])