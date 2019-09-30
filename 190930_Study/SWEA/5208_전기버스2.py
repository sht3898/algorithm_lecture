import sys; sys.stdin = open('5208_input.txt', 'r')

'''
1번 정류장에서 선택지
    - 충전지 장착하고 2번 정류장으로 이동

2번 정류장에서의 선택지
1) 충전기 교체하고 다음 정류장으로 이동 => 충전지 잔량이 1 이상
2) 교체하지 않고 다음 정류장으로 이동
'''


def path(cur, elec, cnt):   # cur: 정류장번호, elec : 충전량, cnt: 교체 횟수
    global ans
    if cnt >= ans: return
    if cnt >= arr[0]:
        ans = cnt
    else:
        if elec > 0:
            path(cur+1, elec-1, cnt)
        path(cur+1, arr[cur]-1, cnt+1)


for TC in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    ans = arr[0]
    M = arr[1:]
    visited = [0] * ans
    battery = M[0]
    charge = 0
    min_charge = 0xffffff
    path(1, battery, 0)
    print('#{}'.format(TC),end=' ')
    print(ans)