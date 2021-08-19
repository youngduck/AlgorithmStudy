while True:
    n=int(input())
    
    if n == 0:
        break
        
    num_range=[True]*(2*n+1)
    
    num_range[0]=False
    num_range[1]=False
    
    i=2
    while i <= (2*n)**(1/2)+1:
        if num_range[i]:
            j=i*i
            while j <= 2*n:
                num_range[j]=False
                j+=i
        i+=1
    cnt=0
    for i in range(n+1,2*n+1):
        if num_range[i]:
            cnt+=1
    print(cnt)