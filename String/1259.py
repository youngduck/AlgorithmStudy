import sys

while True:
    num=sys.stdin.readline().rstrip()
    if num == '0':
        break
    if list(num)==list(reversed(num)):
        print('yes')
    else:
        print('no')