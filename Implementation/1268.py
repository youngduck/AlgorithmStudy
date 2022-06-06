import sys

student_num=int(sys.stdin.readline())
student_cnt=[0]*(student_num)

grade=[[],[],[],[],[]]

s={}

for i in range(student_num):
    data=list(map(int,sys.stdin.readline().split()))
    s[i]=[]
    grade[0].append(data[0])
    grade[1].append(data[1])
    grade[2].append(data[2])
    grade[3].append(data[3])
    grade[4].append(data[4])

for j in s:
    for k in grade:
        if k.count(k[j])>=2:
            meet=list(filter(lambda x:k[x]==k[j],range(len(k))))
            s[j]=list(set(s[j]+meet))
    if j in s[j]:
        s[j].remove(j)

result=[]

for i in s:
    result.append(len(s[i]))

print(result.index(max(result))+1)
