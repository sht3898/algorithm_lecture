import sys
sys.stdin = open('flatten.txt', 'r')

for tc in range(10):
    chance = int(input())
    box = list(map(int, input().split()))
    if chance > 0:
        for idx in range(len(box)):
            high = max(box)
            low = min(box)
            if box[idx] == high:
                box[idx] -= 1
            if box[idx] == low:
                box[idx] += 1
            print(high, low)
            chance -= 1

    print('#{} {}'.format(tc+1, high - low))
