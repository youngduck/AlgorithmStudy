import sys
from itertools import combinations



while(True):
    case=list(map(int,sys.stdin.readline().split()))
    k=case[0]
    data=case[1:]
    if k ==0:
        break
    for i in list(combinations(data,6)):
        print(*i)
    print()
