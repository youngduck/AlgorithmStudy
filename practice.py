from collections import Counter

x=Counter({5:1,6:2,7:3})
y=Counter({5:1,6:2,7:3})
result=dict(x+y)

print(max(result,key=result.get))
print(result)
print(max(result.keys()))