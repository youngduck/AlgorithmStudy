import sys

n=int(sys.stdin.readline())

#한칸에 하나의 퀸만오므로 1차원배열만으로 표시가능 index는 행,index안의 값은 열의 위치!
data=[0]*n


def nq(index,n,data):

    result=0
    if index == n:
        return 1

    #for/else 구문 사용.
    for i in range(n):
        data[index]=i
        for j in range(index):
            #같은 열에 있는지 확인
            if data[j]==data[index]:
                break
            #대각선에 있는지 확인 -> 2차원배열속 index 값들의 합,차를 이용해서 대각선판별함.
            if abs(data[index]-data[j])==index-j:
                break
        else:
            result+=nq(index+1,n,data)
    return result

print(nq(0,n,data))

# https://rebas.kr/761 대각선을 배열로미리만들어서 판별하기.