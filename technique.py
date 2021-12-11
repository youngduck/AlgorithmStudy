#-----출력시
#배열 a를 print(*a) 로 출력하면 알맹이들만 이쁘게나옴.

#import heapq

#-----import numpy   백준에서 numpy 사용할수없음...
#numpy.dot() -> 행렬계산 -> 2740.py 참조
#numpy.ndim() -> n차원행렬의 n반환
#data=numpy.array(data)
#print(data.shape) -> n행m열 (n,m) 튜플출력

#------from itertools import 순열,조합~
#누적합-> from itertools import accumulate

#-----import math

#-----배열관련
#list(filter(함수,리스트))  -> 리스트에서 원하는 함수를 만족하는 값 여러개(리스트로)반환해줌.

#------내장함수 zip
#numbers=[1,2,3]
#letters=["a","b","c"]
##pairs=zip(numbers,letters)
##for i in zip(nmbers,letters):
#    print(i)
#(1,"a")
#(2,"b")
#(3,"c")

#---------3차원이내 외적 == 방향성을 갖는 법선벡터
#외적값-> 음수: 반시계방향 0:직선 양수: 시계방향 의미