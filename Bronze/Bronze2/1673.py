while True:
    try:
        n,k=map(int,input().split())
        chicken=0
        coupon=n
        stamp=0
      
        while True:
            chicken += coupon
            stamp+=coupon
            coupon=0

            if coupon == 0 and stamp < k:
                break
            else:
                coupon=stamp//k
                stamp=stamp%k
        print(chicken)
    except:
        break