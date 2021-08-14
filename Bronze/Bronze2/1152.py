n=list(map(str,input().split(' ')))
result=len(n)
if n[0] == '':
    result-=1
if n[-1]=='':
    result-=1
print(result)