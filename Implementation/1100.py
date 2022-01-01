import sys

board=[list(sys.stdin.readline().rstrip()) for i in range(8)]
cnt=0

for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and board[i][j]=='F':
            cnt+=1
print(cnt)