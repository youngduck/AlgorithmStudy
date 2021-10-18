import sys

n=int(sys.stdin.readline())
data=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pass_cnt=[0]*53
word_cnt=[0]*53
#0띄어쓰기'
#1~26 : A~Z 
#27~52 : a~z로 해석 한다.

password=list(map(int,sys.stdin.readline().split()))
word=list(sys.stdin.readline().rstrip())

for i in password:
    pass_cnt[i]+=1

for i in word:
    word_cnt[data.index(i)]+=1

if pass_cnt == word_cnt:
    print("y")
else:
    print("n")