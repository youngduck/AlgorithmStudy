import sys

t=int(sys.stdin.readline())

for i in range(t):
    word=sys.stdin.readline()
    cnt=0
    for j in word:
        if j == '(':
            cnt+=1
        elif j == ')':
            cnt-=1
        if cnt <0:
            cnt=-1
            break
            
    if cnt == 0:
       print("YES")
    else:
       print("NO")

