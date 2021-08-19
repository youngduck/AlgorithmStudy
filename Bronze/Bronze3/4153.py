while True:
    num=list(map(int,input().split()))
    num=sorted(num)  
    if num[0]==0:
        break
    elif num[0]**2+num[1]**2==num[2]**2:
        print("right")
    else:
        print("wrong")