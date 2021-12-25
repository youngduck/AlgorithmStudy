
while True:
    try:
        a=int(input())
        if a % 6 == 0:
            print("Y")
        else:
            print("N")
    except:
        break