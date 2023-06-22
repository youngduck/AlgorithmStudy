import sys

def findIndex(x):
    if(binury_num[binury_num_length-x-1]=='1'):
        return str(x)
    
for i in range(int(sys.stdin.readline())):
    binury_num=bin(int(sys.stdin.readline()))
    binury_num_length=len(binury_num)

    filterd_data=list(filter(findIndex,range(binury_num_length-2)))
    print(*filterd_data)


