# 2. 배열 2(Array 2)

## 2차원 배열

* 부분집합의 수

  {1} => 0 0 0 => 0

  {2} => 1 0 0 => 4

  . . .

  {2, 3} => 0 1 1 => 5

  {1, 2, 3} => 1 1 1 => 7



## 비트 연산자

`&` : 비트 단위로 and 연산

`|` : 비트 단위로 or 연산

`<<` : 피연산자의 비트 열을 왼쪽으로 이동

`>>`: 피연산자의 비트 열을 오른쪽으로 이동

비트 연산자는 숫자 앞에 0b 가 붙는다. (b는 binary)

10진수 => 0o1111

16진수 => 0x1111

* `<<` 연산자
  * 1 << n : 2ⁿ 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미
* `<<` 연산자
  * 2로 나눈 것과 같은 결과



* 비트 연산자 계산

```python
a = 0b1010
b = 0b1100
print(bin(a & b))
# => 0b1000
print(bin(a << 1)) 
# => 0b10100 원래 a 값에 2^1 을 곱한 값과 같음
print(bin(a << 2))
# => 0b10111 원래 a 값에 2^2 을 곱한 값과 같음
```



* 더 빠르게 홀짝 여부 연산하는 방법

```python
n=10
if n & 1:
    print('홀수')
else:
    print('짝수')
```



## 부분 집합 생성

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # 원소의 개수
for i in range(1<<n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
        print()
    print()
```





## 검색

### 순차 검색(Sequential Search)

일렬로 되어 있는 자료를 순서대로 검색하는 방법

* 정렬되어 있지 않은 경우 시간 복잡도: O(n)
* 정렬되어 있는 경우 시간 복잡도 : O(n)



### 이진 검색(Binary Search)

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

* 반복으로 구현

```python
def binarySearch(arr, key):
    lo, hi = 0, len(arr) -1
    # lo = 범위의 시작 인덱스, hi = 범위의 끝 인덱스
    while lo <= hi:
        mid = (lo + hi) >> 1 # //2와 결과가 같음 
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return False          
```

* 재귀로 구현

```python
def binarySearch(arr, lo, hi, key):
    if lo > hi: return False
    
    mid = (lo + hi) >> 1
    
    if arr[mid] == key:
        return True
    elif arr[mid] > key:
        return binarySearch(arr, lo, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, hi, key)
```



## 선택정렬(Selection sort)

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

시간 복잡도 : O(n²)

* 알고리즘 전개과정

```python
arr = [64, 25, 10, 22, 11]
n = len(arr)
# 첫번째 단계 [0, n - 1]
minIdx = 0
for j in range(1, n):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[0], arr[minIdx] = arr[minIdx], arr[0]

# 두번째 단계 [1, n - 1]
minIdx = 1
for j in range(2, n):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[0], arr[minIdx] = arr[minIdx], arr[0]

# ...

print(arr)
```

* 알고리즘

```python
arr = [64, 25, 10, 22, 11]
n = len(arr)

for i in range(n-1): # 0 ~ n-2
    minIdx = i
    for j in range(i + 1, n):
    	if arr[minIdx] > arr[j]:
        	minIdx = j
	arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)
```



## 셀렉션 알고리즘(Selection Algorithm)

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.

시간 복잡도 : O(kn)

* 알고리즘

```python
def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
```



## 인덱스

테이블에 대한 동작 속도를 높여주는 자료 구조

