n=input()
cnt=len(n)
a=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in a:
    n=n.replace(i,'*')
print(len(n))