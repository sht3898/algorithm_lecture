import sys; sys.stdin = open('5208_input.txt', 'r')


def solve(num, station, cnt):
    global result
    if cnt >= result:   # cnt 가 result 보다 크다면 비교할 필요가 없으므로 리턴
        return
    if num + station > len(arr)-1:  # 현재 정류장(num)부터 갈수 있는 거리가 전체 길이보다 길다면
        result = cnt    # result 를 cnt 로 바꿔서 저장하고 리턴
        return
    for j in range(num + 1, num + station + 1):  # 현재 정류장부터 갈 수 있는 정류장까지 반복하면서
        solve(j, arr[j], cnt+1)  # 재귀를 통해 정답 도출
    # for j in range(i+1, num+i+1):
    #     back(j, station[j], count+1)


for TC in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    result = len(arr)-1
    solve(1, arr[1], 0)
    print('#{} {}'.format(TC, result))

