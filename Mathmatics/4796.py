i=1

while True:  
    result=0
    L,P,V=map(int,input().split())
    
    if L+P+V==0:
        break
        
    result+=L*(V//P)
    if L>V%P:
        result+=V%P
    else:
        result+=L
        
    print("Case %d: %d" %(i,result))
    i+=1
