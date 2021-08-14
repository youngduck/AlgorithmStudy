#1157
n=input()
N=n.upper()
alpha=[chr(t) for t in range(65,91)]
a=[]
f=0
for i in alpha:
    cnt=N.count(i)
    a.append(cnt)
m=max(a)
for i in a:
    if i == m:
        f+=1
if f==1:
    result=alpha[a.index(m)]
    print(result)
if f>=2:
    print("?")