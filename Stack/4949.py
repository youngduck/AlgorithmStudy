import sys
from collections import deque

bracket = ['[',']','(',')']

def isBracket(x):
    if x in bracket:
        return True

while True:
    word = sys.stdin.readline().rstrip()
    
    stack=deque([])
    
    if word == '.':
        break
    
    result = True

    filterdData=deque(filter(isBracket,word))
    while (filterdData):
        filteredWord = filterdData.popleft()
        if filteredWord == '[' or filteredWord =='(':
            stack.append(filteredWord)
        elif filteredWord == ']':
            if len(stack) !=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']')
        else:
            if len(stack) !=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                break

    if ((len(stack)==0)):
        print('yes')
    else:
        print('no')
