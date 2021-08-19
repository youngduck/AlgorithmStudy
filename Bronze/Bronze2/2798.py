n,m=map(int,input().split())
n_list=list(map(int,input().split()))
result=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or j==k or k==i:
                pass
            else:
                test=n_list[i]+n_list[j]+n_list[k]
                if test>result and m>=test:
                    result=n_list[i]+n_list[j]+n_list[k]
                
print(result)