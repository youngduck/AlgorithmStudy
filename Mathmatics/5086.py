import sys

while True:
    a,b = map(int,sys.stdin.readline().split())

    #두수는 같지않은 자연수
    if a+b==0:
        break

    #약수테스트
    if (a<b and b%a == 0):
        print("factor")
    #배수테스트
    elif (a>b and a%b==0):
        print("multiple")
    else:
        print("neither")



