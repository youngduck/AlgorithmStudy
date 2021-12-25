#상수의 대답출력 상수는abc를 cba로읽음
n1,n2=map(int,input().split(' '))
def sangsu(n):
    return (n%10*100)+(n//10%10*10)+(n//100)
n1=sangsu(n1)
n2=sangsu(n2)
if n1>n2:
    print(n1)
else:
    print(n2)