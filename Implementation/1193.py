#1193
x=int(input())
a=[]
b=[]
n=1
result=0
while True:    
    result+=n
    if result>=x:   
        break
    n+=1
for i in range(1,n+1):
    a.append(i)
    b.append(i)
if n%2 !=0:
    a=sorted(a,reverse=True)
else :
    b=sorted(b,reverse=True)
k=x-(result-n)-1
a=a[k]
b=b[k]
print("%d/%d" %(a,b))