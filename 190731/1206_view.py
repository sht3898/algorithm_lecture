import sys
sys.stdin = open('input.txt', 'r')  # input을 읽어와서 한줄씩 읽음

# 빌딩 개수만큼 반복
for tc in range(1, 11):
    n = int(input())  # 테스트 코드 개수 입력
    buildings = list(map(int, input().split()))  # 빌딩의 높이를 입력 받아 int형태로 바꾼 후 buildings에 리스트 형태로 저장
    result = 0  # 결과를 저장하기 위한 result 값 생성
    for i in range(2, n-2):  # 높이가 0인 처음과 마지막 두 칸을 제외하고 반복
        high = buildings[i-2]  # 반복에서 처음 시작되는 부분을 high 로 설정하고 높이 비교에 사용
        for j in range(i-2, i+3):  # 현재 빌딩의 앞, 뒤 두 빌딩을 반복
            if j == i:
                continue  # 반복문에서 현재 빌딩이 걸린다면 넘어가기
            if buildings[j] > high:  # 비교하는 빌딩의 높이와 현재 최고 높이를 비교하여 더 큰 값을 저장
                high = buildings[j]
        if buildings[i] > high:  # 현재 빌딩의 높이와 최고 높이를 비교하여 지금 빌딩이 더 높다면 다음으로 높은 빌딩과의 높이 차를 결과에 저장
            result += buildings[i] - high
    print('#{} {}'.format(tc, result))  # 결과 출력
