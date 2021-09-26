import sys

data=[[1,3],[3,4],[1,4]]
n=int(sys.stdin.readline())

if n == 3:
    for i in range(n):
        finger=list(map(int,sys.stdin.readline().split()))
        finger.sort()
        if finger in data:
            data.pop(data.index(finger))
    if not data:
        print("Wa-pa-pa-pa-pa-pa-pow!")
    else:
        print("Woof-meow-tweet-squeek")
else:
    print("Woof-meow-tweet-squeek")



