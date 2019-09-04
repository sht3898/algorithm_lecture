# 모음 자음 출력

# 4 6
# a t c i s w
import sys;

sys.stdin = open('1759_input.txt', 'r')

pwd = []  # pwd: 전역 변수, 부분 집합에 들어갈 원소 저장
alpha = ('a', 'e', 'i', 'o', 'u')


def backtrack(k, mo, ja):  # k: 넣을 원소의 인덱스, mo: 모음, ja: 자음
    if len(pwd) == L:  # 추가하는 원소가 L개가 되면 더 이상 찾을 필요 없음
        print(*pwd)
        return
    if k == C: return

    pwd.append(arr[k])
    a = b = 0
    if arr[k] in alpha:
        a = 1
    else:
        b = 1
    backtrack(k + 1, mo + a, ja + b)  # k번째 요소를 포함하는 경우


    pwd.pop()
    backtrack(k + 1, mo, ja)  # k번째 요소를 포함하지 않는 경우
L, C = map(int, input().split())
arr = input().split()
arr.sort()

backtrack(0, 0, 0)