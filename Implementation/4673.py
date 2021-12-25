a=[]
b=[]
n_sum=0
i=1

while (i<=10000):
    b.append(i)
    str_i=str(i)
    n_sum=0
    for j in str_i:
        n_sum+=int(j)
    self_num=i+n_sum
    a.append(self_num)
    i+=1
    
for i in b:
    if i not in a:
        print(i)
        