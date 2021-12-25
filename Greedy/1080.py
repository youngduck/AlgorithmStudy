n,m=map(int,input().split())

a=[]
b=[]
cnt=0



            
#행렬 a 기본 설정
for i in range(n):
    line=input()
    a.append(list(line))

#행렬 b 기본 설정
for i in range(n):
    line=input()
    b.append(list(line))

#뒤집기 함수
def reverse(i,j):
    for y in range(i,i+3):
        for x in range(j,j+3):
            if a[y][x] == '0':
                a[y][x] ='1'
            else:
                a[y][x] ='0'
                

#뒤집기
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            reverse(i,j)
            cnt+=1

#마지막 체크
if a != b:
    cnt=-1

print(cnt)