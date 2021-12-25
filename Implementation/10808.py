s=input()

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt=[0]*26
for i in s:
    cnt[alphabet.index(i)]+=1
for i in cnt:
    print(i,end=' ')