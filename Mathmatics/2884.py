h,m=map(int,input().split())

if h == 0:
    if m<45:
        h=23
        print(h,60+m-45)
    else:
        print(h,m-45)
else :
    if m<45:
        print(h-1,60+m-45)
    else:
        print(h,m-45)