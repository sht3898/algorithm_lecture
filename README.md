# 알고리즘 정리

## 190731_List

### Solving Club

* [1206_view](./190731_List/1206_view.py)



## 190801_List

### Solving Club

* [1208_flattern](./190731_List/1208_flattern.py)



### Course

* [4828_minmax](./190801_List/4828_minmax.py)
* [4831_전기버스](./190801_List/4831_전기버스.py)
* [4831_전기버스_2](./190801_List/4831_2_전기버스.py)
* [4834_숫자카드](./190801_List/4834_숫자카드.py)
* [4835_구간합](./190801_List/4835_구간합.py)



## 190807_List

### Solving Club

* [1209_sum](./190731_List/1209_sum.py)



## 190808_List

### Solving Club

* [1259_금속막대](./190808_List/1259_nasa.py)



### Course

* [4836_색칠하기](./190808_List/4836_겹치는 부분 계산.py)

* [4837_부분집합의 합](./190808_List/4837_부분집합의합.py)

* [4839_이진탐색](./190808_List/4839_이진탐색.py)

* [4843_특별한 정렬](./190808_List/4843_앞뒤하나씩출력.py)

  

## 190814_String

### Solving Club

* [1221_GNS](./190814_String/1221_GNS.py)

* [1946_zip](./190814_String/1946_zip.py)





## 190816_String

### Solving Club

* [1215_회문1](./190816_String/1215_회문1.py)
* [1215_회문1_선생님](./190816_String/1215_회문1_t.py)
* [1216_회문2](./190816_String/1216_회문2.py)

* [1216_회문2_선생님](./190816_String/1216_회문2_t.py)



### Course

* [4864_문자열비교](./190816_String/4864_문자열비교.py)

* [4861_회문](./190816_String/4861_회문.py)

* [4865_글자수](./190816_String/4865_글자수.py)

  



## 190816_추가문제

### Solving Club

* [4408_자기방으로 돌아가기](./190816_String/4408_수련회.py)
* [4522_세상의 모든 펠린드롬](./190816_String/4522_팰린드롬1.py)
* [4579_세상의 모든 펠린드롬2](./190816_String/팰린드롬2.py)





## 190821_Stack1

### Solving Club

* [1210_Ladder1](./190821_Stack1/1210_Ladder1.py)

* [1267_작업순서](./190821_Stack1/1267_작업순서.py)

* [1267_작업순서_study](./190821_Stack1/1267_작업순서_study.py)

  ```python
  from collections import deque       # queue 사용
  
  
  def bfs(graph):                     # bfs 그래프
      q = deque()
      for i in range(1, V+1):     # 꼭지점의 개수만큼 반복
          if degree[i] == 0:      # 꼭지점의 깊이가 0이라면 q에 저장
              q.append(i)     
      while q:        # q의 길이가 0 이상일때 반복
          temp = q.popleft()      # 현재 큐의 첫번째 원소를 pop
          result.append(temp)     # result 에 꺼낸 원소를 저장
          for w in graph[temp]:   # 꺼낸 원소의 다음 경로를 반복
              if degree[w] != 0:  # 깊이가 0이 아니라면 깊이를 1 감소시켜 
                  				# 다음 경로로 진출할 수 있게 만듦
                  degree[w] -= 1
                  if degree[w] == 0:  # 깊이가 0이라면 q에 저장하여 반복시킴
                      q.append(w)
  
  
  for TC in range(1, 11):
      V, E = map(int, input().split())
      arr = list(map(int, input().split()))
      G = [[] for _ in range(V + 1)]
      result = []
      start = []
      degree = [0] * (V + 1)
      for i in range(E):
          G[arr[2 * i]].append(arr[2 * i + 1])
          degree[arr[2*i+1]] += 1     # 깊이 저장
  
      bfs(G)
  
      print('#{}'.format(TC), end=' ')
      print(*result)
  ```

  

* [5432_쇠막대기 자르기](./190821_Stack1/5432_쇠막대기.py)

* [5432_쇠막대기 자르기_Stack](./190821_Stack1/5432_쇠막대기_stack.py)

  ```python
  import sys; sys.stdin = open('5432_input.txt', 'r')
  
  T = int(input())
  
  for TC in range(1, T+1):
  
      arr = input()
      stack = []
      result = 0
  
      for token in arr:
          if token == '(':
              stack.append(token)
              last = token
          else:
              if last == '(': # 이전 막대기와 비교
                  stack.pop()
                  result += len(stack)
                  last = token
              else:           # 막대기의 끝
                  stack.pop()
                  result += 1
      print('#{}'.format(TC), end=' ')
      print(result)
  ```

  



### Course

* [4869_종이붙이기](./190821_Stack1/4869_종이붙이기.py)
* [4866_괄호검사](./190821_Stack1/4866_괄호검사.py)
* [4871_그래프경로](./190821_Stack1/4871_그래프경로.py)
* [4873_반복문자지우기](./190821_Stack1/4873_반복문자_지우기.py)



## 190826~27_Stack2

### Solving Club

* [1220_Magnetic](./190826_Stack2/1220_magnetic.py)
* [1224_계산기3](./190827_Stack2/1224_계산기3.py)



### Course

* [4874_Forth](./190827_Stack2/4874_forth.py)
* [4875_미로](./190827_Stack2/4875_미로.py)
* [4875_미로 재귀](./190827_Stack2/4875_미로_재귀.py)
* [4875_미로 재귀2](./190827_Stack2/4875_미로_재귀2.py)
* [4880_카드게임](./190827_Stack2/4880_카드게임.py)
* [4880_카드게임2](./190827_Stack2/4880_카드게임_2.py)
* [4881_배열 최소 합](./190827_Stack2/4881_배열최소합.py)
* [4881_배열 최소 합_1](./190827_Stack2/4881_배열최소합_1.py)
* [4881_배열 최소 합_2](./190827_Stack2/4881_배열최소합_2.py)



## 190828_Queue

### Solving Club

* [1238_Contact](./190828_Queue/1238_contact.py)
* [4047_카드카운팅](./190828_Queue/4047_카드카운팅.py)



### Course

* [5097_회전](./190828_Queue/5097_회전.py)
* [5105_미로의거리](./190828_Queue/5105_미로의거리.py)
* [5099_피자굽기]
* [5102_노드의거리]



## 190902_List

### Solving Club

* [1258_행렬찾기](./190902_List/1258_행렬찾기.py)

  ```python
  # 선생님 방법
  ans = []
  
  for i in range(N):
      for j in range(N):
          if arr[i][j] == 0: continue
          
          r, c = i, 0		# r: 행, c: 열
          while r < N and arr[r][j]:
              c = j
              while c < N and arr[r][c]:
                  arr[r][c] = 0
                  c += 1
              r += 1
              
          ans.append((r - i, c - j))
          
  ans.sort(key= lambda a: (a[0] * a[1], a[0]))
  # lambda를 사용하면 정렬할 때 순위를 지정할 수 있음
  # a[0] * a[1]가 1순위, a[0]가 2순위
  ```

  

* [6485_버스노선]



### Course

* [5108_숫자추가](./190902_List/5105_숫자추가.py)
* [5110_수열합치기](./190902_List/5110_수열합치기.py)
* [5120_암호](./190902_List/5120_암호.py)
* [5122_수열편집]



### BOJ

* [1759 암호만들기](./190902_List/1759_암호만들기.py)

  6개 중 4개 골라내면 조합, 4개 골라 순서대로 나열하면 순열

  ```python
  # 선생님 풀이
  # 6C4의 원소들을 모두 출력
  # 부분 집합으로 풀이
  
  # 4 6
  # a t c i s w
  import sys; sys.stdin = open('1759_input.txt', 'r')
  
  pwd = []	# pwd: 전역 변수, 부분 집합에 들어갈 원소 저장
  def backtrack(k):	# k: 넣을 원소의 인덱스
      if len(pwd) == L:	# 추가하는 원소가 L개가 되면 더 이상 찾을 필요 없음
          print(pwd)
          return
      if k == C: return
      
      pwd.append(arr[k])
  	backtrack(k+1)	# k번째 요소를 포함하는 경우
      pwd.pop()
      backtrack(k+1)	# k번째 요소를 포함하지 않는 경우
  L, C = map(int, input().split())
  arr = input().split()
  arr.sort()
  
  backtrack(0)
  ```

  ```python
  # 모음 자음 출력
  
  # 4 6
  # a t c i s w
  import sys; sys.stdin = open('1759_input.txt', 'r')
  
  pwd = []	# pwd: 전역 변수, 부분 집합에 들어갈 원소 저장
  alpha = ('a', 'e', 'i', 'o', 'u')
  def backtrack(k, mo, ja):	# k: 넣을 원소의 인덱스, mo: 모음, ja: 자음
      if len(pwd) == L:	# 추가하는 원소가 L개가 되면 더 이상 찾을 필요 없음
          print(pwd)
          return
      if k == C: return
      
      pwd.append(arr[k])
      a = b = 0
      if arr[k] in alpha: a = 1
      else: b = 1
  	backtrack(k+1, mo + a, ja + b)	# k번째 요소를 포함하는 경우
      pwd.pop()
      backtrack(k+1, mo, ja)	# k번째 요소를 포함하지 않는 경우
  L, C = map(int, input().split())
  arr = input().split()
  arr.sort()
  
  backtrack(0, 0, 0)
  ```

  ```python
  # 조합 생성
  # 3C2
  
  # 중복 순열 3Pi2
  # 순열 3P2
  # 조합 3C2
  # 중복 조합 3H2
  
  arr = 'ABC'; N = len(arr)
  for i in range(N):
      for j in range(N):
          if i == j: continue
          print(arr[i], arr[j])
  ```

  ```python
  # 조합 생성 방법, 이전에 했던 것은 출력됐기 때문에 할 필요 없음
  arr = 'ABC';N = len(arr)
  
  for i in range(N):
      for j in range(i + 1, N):
          print(arr[i], arr[j])
  ```

  ```python
  # 중복 조합
  
  arr = 'ABC';N = len(arr)
  
  for i in range(N):
      for j in range(i, N):
          print(arr[i], arr[j])
  ```

  ```python
  # 5C3
  
  arr = 'ABCDE';N = len(arr)
  
  for i in range(N):
      for j in range(i + 1, N):
          for k in range(j + 1, N):
          	print(arr[i], arr[j], arr[k])
  ```

  ```python
  # 5C3 재귀
  arr = 'ABCDE'; N = len(arr)
  N, R = 5, 3
  choose = []
  
  def comb(k, start):		# k: 지금까지 선택한 개수, start: 반복문의 시작값
      if K == R:
          return
      for i in range(start, N):
          choose.append(arr[i])
          # i번째 정보를 저장
          comb(k + 1, i + 1)
          choose.pop()
  
  comb(0, 0)
  ```

  ```python
  # 5H3(중복조합) 재귀
  arr = 'ABCDE'; N = len(arr)
  N, R = 5, 3
  choose = []
  
  def comb(k, start):		# k: 지금까지 선택한 개수, start: 반복문의 시작값
      if K == R:
          return
      for i in range(start, N):
          choose.append(arr[i])
          # i번째 정보를 저장
          comb(k + 1, i)	# i번도 가능하게 포함시킴
          choose.pop()
  
  comb(0, 0)
  ```

  



## 190904_Study

### BOJ

* [1769_암호만들기](./190904_Study/1697_숨바꼭질.py)

* [1697_숨바꼭질](./190904_Study/1697_숨바꼭질.py)

  ```python
  # dfs로 풀면 시간이 초과되기 때문에 bfs로 풀어야함
  def bfs(v):
      visit = [0] * 100001
      q = [v]
      cnt = 0
      state = 0
  
      while q:
          for _ in range(len(q)):
              v = q.pop(0)
              if not visit[v]:
                  visit[v] = 1
                  if v == K:
                      state = 1
                      break
                  if v - 1 >= 0:
                      q.append(v - 1)
                  if v + 1 <= 100000:
                      q.append(v + 1)
                  if v * 2 <= 100000:
                      q.append(v * 2)
  
          if state:
              print(cnt)
              break
          cnt += 1
  
  
  N, K = map(int, input().split())
  bfs(N)
  ```

  ```python
  # dfs ver
  N, K = map(int, input().split())
  D = [100000] * 100001
  
  def find(x):
      print(x)
  	if D[x] >= D[K]: return
      
  ```

* [14501_퇴사](./190904_Study/14501_퇴사.py)

* [5427_불](./190904_Study/5427_불.py)




## 190905_Study

### BOJ

* [1260_탐색알고리즘](./190905_Study/1260_탐색알고리즘.py)
* [2589_보물섬](./190905_Study/2589_보물섬.py)
* [2606_바이러스](./190905_Study/2606_바이러스.py)
* [2667_단지번호붙이기](./190905_Study/2667_단지번호붙이기.py)



## 190918_시작하기

### BOJ

* [2606_바이러스](./190918_시작하기/BOJ/2606_바이러스.py)
* [2667_단지번호](./190918_시작하기/BOJ/2667_단지번호.py)
* [10026_적록색약](./190918_시작하기/BOJ/10026_적록색약.py)
  * 재귀로 하면 런타임 에러
  * 예외 조건 처리를 잘해야함
* [1405_미친로봇](./190918_시작하기/BOJ/1405_미친로봇.py)
  * 백트래킹 활용
* [1405_미친로봇2](./190918_시작하기/BOJ/1405_미친로봇2.py)
  * 내가 직접 푼 것



### Solving Club

* [1240_단순2진암호](./190918_시작하기/solvingclub/1240_단순2진암호.py)
* [1242_암호코드스캔](./190918_시작하기/solvingclub/1242_암호코드스캔.py)
* [4366_은행업무](./190918_시작하기/solvingclub/4366_은행업무.py)
  * int(문자열 숫자, 진수) => 숫자가 주어진 진수라고 했을때 10진수로 변환하면 나오는 수
  * ex) int(13, 9) => 1x9 + 3x1 => 14 

### Swea

* [1210_ladder1](./190918_시작하기/1210_ladder1.py)
* [4613_러시아국기](./190918_시작하기/4613_러시아국기.py)
  * 완전 탐색 활용
* [4875_미로](./190918_시작하기/4875_미로.py)



## 190919_보충

### BOJ

* [15649_N과M1](./190919_보충/BOJ/15649_N과M1.py)
* [15650_N과M2](./190919_보충/BOJ/15650_N과M2.py)
* [15650_N과M2v2](./190919_보충/BOJ/15650_N과M2v2.py)
  * 이건 시간 복잡도가 높아서 좋지 않음
* [15651_N과M2](./190919_보충/BOJ/15651_N과M3.py)
* [15652_N과M2](./190919_보충/BOJ/15651_N과M4.py)

