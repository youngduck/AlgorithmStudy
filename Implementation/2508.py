import sys

t=int(input())


for i in range(t):
    input()
    r,c=map(int,input().split())
    box=[]
    cnt=0
    for i in range(r):
        box.append(input())
    b = -1

    for data in box:
        a=list(filter(lambda x:data[x] == 'o',range(len(data))))
        b += 1

        for i in a:
            try:
                if data[i-1] + data[i] + data[i+1] =='>o<':
                    cnt+=1
            except:
                print('',end='')
        for i in a:
            try:
                if box[b-1][i]+box[b][i]+box[b+1][i] =='vo^':
                    cnt+=1
            except:
                print('',end='')
    print(cnt)

