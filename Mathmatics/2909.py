#정수부분 반올림

C,K=map(int,input().split())

#print(round(C,-K))  <-이거 왜 틀리는지 이해가 안됨.
print(int(round(C+0.1,-K)))