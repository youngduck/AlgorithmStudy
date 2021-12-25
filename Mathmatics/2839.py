N=int(input())
mul_5=N//5
mul_3=N//3

a=[i+j for i in range(mul_5+1) for j in range(mul_3+1) if i*5+j*3==N]

if a==[]:
    result=-1
else:
    result=min(a)
print(result)