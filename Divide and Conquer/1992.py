import sys
n=int(sys.stdin.readline())
data=[ list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

def quadtree(x,y,n):
    check=data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[x][y] != data[i][j]:
                print("(",end='')
                quadtree(x,y,n//2)
                quadtree(x,y+n//2,n//2)
                quadtree(x+n//2,y,n//2)
                quadtree(x+n//2,y+n//2,n//2)
                print(")",end='')
                check=-1
                break
        if check == -1:
            break
        

    if check==1:
        print(1,end='')
    elif check == 0:
        print(0,end='')


quadtree(0,0,n)