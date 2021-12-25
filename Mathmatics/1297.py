import sys

#D:대각선길이 H:높이비율 W:넓이비율

D,H,W=map(int,sys.stdin.readline().split())

makit_real=D/((H**2+W**2)**(1/2))

real_H=int(makit_real*H)
real_W=int(makit_real*W)

print(real_H,real_W)