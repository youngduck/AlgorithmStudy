import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))


A.sort()

def find(data):      
    for i in data:
        left=0
        right=len(A)-1
        while True:
            mid = (left+right)//2
            if i < A[mid]:
                right = mid-1
            elif i > A[mid]:
                left = mid+1 
            else :
                print(1)
                break
            if left> right:
                print(0)
                break
    
find(data)