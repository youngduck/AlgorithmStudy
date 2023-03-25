import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    word=deque(sys.stdin.readline().rstrip())
    cnt = 0
    result='NO'
    while(word):
        wordPop=word.pop()
        if wordPop==')':
            cnt+=1
        else:
            cnt-=1
            if(cnt<0):
                break
    if(cnt==0):
        result='YES'
    print(result)
