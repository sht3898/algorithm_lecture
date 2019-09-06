import sys
sys.stdin = open('bin.txt', 'r')

# set은 이진탐색트리, 해싱 => 더 빨라질수 있음

def binary_search(page, target):
    low = 1
    mid = (low + page)//2
    count = 0
    while mid != target:
        if mid < target:
            low = mid
        else:
            page = mid
        mid = (low + page)//2
        count += 1
    return count


if __name__ == '__main__':
    tc = int(input())

    for t in range(tc):
        p, a, b = map(int, input().split())
        if binary_search(p, b) > binary_search(p, a):
            print('#{} A'.format(t+1))
        elif binary_search(p, a) > binary_search(p, b):
            print('#{} B'.format(t+1))
        else:
            print('#{} 0'.format(t+1))