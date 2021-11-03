from itertools import combinations

data=[1,2,3,4,5]

for i in range(2,4):
    a=list(combinations(data,i))
    print(a)