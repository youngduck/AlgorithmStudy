import sys

input=sys.stdin.readline().split()
word=''.join(input)

if word =='12345678':
    print('ascending')
elif word =='87654321':
    print('descending')
else:
    print('mixed')