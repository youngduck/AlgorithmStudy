#참외밭 -> 무조건 ㄱ,ㄴ 같은 6각형
#따라서 큰사각형에서 작은 사각형을 빼는 방식으로 풀기로함.
#작은사각형의 변을 찾는법은 바로 앞 뒤변의 합이 큰사각형의 변이랑 같을때이다.
import sys

k=int(sys.stdin.readline())


small_width=0
small_height=0
height_list=[]
width_list=[]
data=[]

#어차피 반시계방향,육각형으로 만들어지므로
for i in range(6):
    dir,dis=map(int,sys.stdin.readline().split())
    if i%2 ==0:
        width_list.append(dis)
    else:
        height_list.append(dis)
    data.append(dis)
        
#작은사각형구하기 홀수,짝수데이터 구분
for i in range(6):
    if i%2==0:
        if max(height_list)==data[(i-1)%6]+data[(i+1)%6]:
            small_width=data[i]
    else:
        if max(width_list)==data[(i-1)%6]+data[(i+1)%6]:
            small_height=data[i]


#큰사각형,작은사각형 결론
largeRect=max(height_list)*max(width_list)
smallRect=small_width*small_height

print(k*(largeRect-smallRect))