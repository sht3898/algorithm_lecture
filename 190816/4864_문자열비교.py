import sys
sys.stdin = open('words.txt', 'r')

tc = int(input())

for t in range(tc):
    pattern = input()  # 찾을 패턴 입력
    text = input()  # 전체 문자열 입력
    m = len(pattern)  # 찾을 패턴의 길이
    n = len(text)  # 전체 문자열의 길이
    i = j = 0  # 패턴과, 문자열의 인덱스
    while j < m and i < n:  # 패턴과 문자열의 길이 만큼 반복
        if text[i] != pattern[j]:  # 문자열과 패턴의 문자가 같을 때
            i = i - j  #  
            j = -1
        i = i + 1
        j = j + 1
    if j == m:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))