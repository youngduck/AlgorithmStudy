a=[]

for i in range(9):
    b=int(input())
    a.append(b)
 

for i in range(9):
    if max(a)==a[i]:
        c=i+1    
print(max(a))
print(c)
