t=int(input())
for i in range(t):
    h,w,n=map(int,input().split(' '))
    if n%h==0:
        floor=h*100
        ho=n//h
    else:
        floor=n%h*100
        ho=n//h+1
    print(floor+ho)