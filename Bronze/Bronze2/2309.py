short=[]

for i in range(9):
    num=int(input())
    short.append(num)
    
short.sort()
full=sum(short)
find=full-100

for i in short:
    for j in short:
        if i ==j:
            continue
        elif i+j == find:
            short.pop(short.index(i))
            short.pop(short.index(j))
    if len(short) == 7:
        break
        
                
for i in short:
    print(i)