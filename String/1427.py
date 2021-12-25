N=input()
num=[]
for i in range(len(N)):
    num.append(int(N[i]))
num.sort(reverse=True)
for i in num:
    print(i,end='')