import sys

n=int(sys.stdin.readline())

student_arr = list(range(1,n+1))
pick_arr=list(map(int,(sys.stdin.readline().split())))

data=zip(pick_arr,student_arr)
result=[]

for pick,student in data:
    result.insert(student-pick-1,student)

print(*result)


# a=[]
# 칸수,학생
# a.insert(0,1)
# a.insert(1-1,2)
# a.insert(2-1,3)
# a.insert(3-3,4)
# a.insert(4-2,5)

# print(a)