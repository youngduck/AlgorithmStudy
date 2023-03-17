## 스택,큐사용시

```py
import heapq
heapq.heappop()
heapq.heapify()
heapq.heappush()
```

## 시간 줄이기

.append() 하는것보다 리스트 여러개를 생성후 직접 값을 할당해주는것이 좋음.
계수정렬 => O(n)

## 출력 잡기술

```py
data=[1,2,3]
print(*data) #1 2 3
```

## from collections

개수 카운터

```py
from collections import Counter

count = Counter(['red','blue','red','yellow','pink','blue'])

print(count['red'])
print(dict(count))

```

## from itertools

```py
from itertools import combinations
from itertools import permutations
from itertools import accumulate
```

## 내장함수 zip

```py
numbers=[1,2,3]
letters=['a','b','c']
pairs=zip(numbers,letters)
for i in pairs:
    print(i)
```

## 두 벡터의 외적값 = n

```py
dir=''
if n>0:
    dir='시계방향'
elif n<0:
    dir='반시계방향'
else:
    dir='직선방향'
```

## list(filter(함수,리스트))

- 리스트에서 원하는 함수를 만족하는 여러값들을 리스트로 반환해줌

## for/else문

- for문안에서 break없이 모두진행되었는지 else문으로 확인해 줄 수 있다.

## 양의 무한대/음의 무한대

```py
p=float('inf')  #양의무한대

m=float('inf') #음의무한대
```

## reverse,reversed
