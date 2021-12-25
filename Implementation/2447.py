import sys

n=int(sys.stdin.readline())

board=[[' ']*n for i in range(n)]

def star(n,row,col):
    if n == 1:
        return
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    board[row+i][col+j]=' '
                else:
                    board[row+i][col+j]='*'
                    
    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    star(n//3,row+n//3*i,col+n//3*j)
        return
star(n,0,0)

for i in range(n):
    print(''.join(board[i]))