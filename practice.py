from itertools import combinations

data=[1,2,3,4]

data2=[2,5,6,2]

for i in zip(data,data2):
    print(i)

data3=list(zip(data,data2))
print(type(data3[2]))

dif=[abs(x-y) for x,y in zip(data,data2)]
print(dif)