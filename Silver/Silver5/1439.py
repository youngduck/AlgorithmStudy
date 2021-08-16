s=input()

cnt=0
cri=int(s[0])
r_cri=1-cri

for i in range(len(s)):
    if cri != int(s[i]):
        if int(s[i]) == r_cri:
            cnt+=1
        cri=int(s[i])
            
print(cnt)