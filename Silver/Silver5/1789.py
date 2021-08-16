num=int(input())

s=0
i=1
cnt=0

while True:  
    s+=i
    if num<s:
      break
    cnt+=1
    i+=1
print(cnt)