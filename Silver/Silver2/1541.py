quiz=input()
a=quiz.split('-')
result = 0

first=a[0].split('+')
for i in first:
    result+=int(i)

for i in a[1:]:
    second=i.split('+')
    for j in second:
        result-=int(j)

print(result)