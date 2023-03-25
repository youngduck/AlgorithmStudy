import sys

#국어 내림차순, 영어 오름차순, 수학점수 내림차순, 이름 오름차순
n=int(sys.stdin.readline())
def stoI(word):
    try:
        return int(word)
    except:
        return word

data=[list(map(stoI,sys.stdin.readline().split())) for i in range(n)]

sorted_data = sorted(data,key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(sorted_data[i][0])