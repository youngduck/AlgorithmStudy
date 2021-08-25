import sys

n=int(sys.stdin.readline())

photoList=[]
photo=[]
result=[]

#그림넣어주기
for i in range(n):
    for j in range(5):
        photo.append(sys.stdin.readline().rstrip())
    photoList.append(photo)
    photo=[]

# 브루트포스
for i in range(len(photoList)):
    for j in range(i+1,len(photoList)):
        cnt=0
        for x in range(5):
            for y in range(7):
                if photoList[i][x][y] !=  photoList[j][x][y]:
                    cnt+=1
        result+=[[i,j,cnt]]


result=sorted(result,key=lambda x:x[2])

print(result[0][0]+1,result[0][1]+1)
