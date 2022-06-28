import sys

#배열만들어서 접근시 메모리초과 => N=15...
#행렬속 규칙을 찾자 4분할 -> 분할정복 

N,r,c=map(int,sys.stdin.readline().split())
result = 0

def shapeZ(n,row,col):
    line=n//2
    global result
    if(line==0):
        return

    
    #1사분면
    if line>row and line>col:
        result+=0
        
    #2사분면    
    elif line>row and line<=col:
        result+=(line**2)
        col-=line
    #3사분면
    elif line<=row and line>col:
        result+=(line**2)*2
        row-=line

    #4사분면
    else:
        result+=(line**2)*3
        col-=line
        row-=line
    shapeZ(line,row,col)
    
        

shapeZ(2**N,r,c)

print(result)
