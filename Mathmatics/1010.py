t=int(input())

def factorial(num):
    if num == 1:
        return 1
    if num == 0:
        return 1
    return num*factorial(num-1)

for i in range(t):
    n,m=map(int,input().split())
    result = factorial(m)/(factorial(m-n)*factorial(n))
    print(int(result))