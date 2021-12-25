N=int(input())
d={}
for _ in range(N):
    word=input()    
    for i in range(len(word)):
        a=len(word)-1
        pt=10**(a-i)
        if word[i] in d :
            d[word[i]]+=pt
        else:
            d[word[i]]=pt
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    
H=0
result=0
for i in range(9,0,-1):
    result +=d[H][1]*i
    H+=1
    if H>=len(d):
        break
print(result)     