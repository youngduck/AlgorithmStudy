import sys

num_list=sys.stdin.readline().split()

result=0

for i in num_list:
    result+=int(i)*int(i)%10
    result%=10
print(result)