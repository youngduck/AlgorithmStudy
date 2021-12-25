import sys

taebo=sys.stdin.readline()

left,right=taebo.split("(")

print(left.count('@'),end=' ')
print(right.count('@'))
