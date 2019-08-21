import sys
sys.stdin = open('bus.txt', 'r')

tc = int(input())


for number in range(tc):
    k, n, m = map(int, input().split())
    '''
    k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    n : 종점 정류장까지의 수
    m : 충전기가 설치된 정류장의 수
    '''
    station = list(map(int, input().split()))
    result = prev = 0
    status = k
    '''
    station : 충전기가 설치된 정류장의 목록
    result : 결과를 저장할 변수
    prev : 이전 정류장의 번호
    status : 전기버스의 충전 상태
    '''
    for i in range(len(station)-1):
        status -= station[i] - prev
        if status < 0:
            result = 0
            break
        if station[i+1] - station[i] > status:
            status = k
            result += 1
        prev = station[i]

    # 마지막 구간 계산
    if result != 0:
        last = station[-1]
        status -= last - prev
        if last - prev > k:
            result = 0
        elif n - last > k:
            result = 0
        elif n - last > status:
            result += 1

    print('#{} {}'.format(number+1, result))
