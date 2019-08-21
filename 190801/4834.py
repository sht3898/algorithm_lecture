import sys
sys.stdin = open('card.txt', 'r')

tc = int(input())

for idx in range(tc):
    card_count = int(input())
    cards = sorted(list(map(int, input())))
    counts = {}
    for number in cards:
        if number not in counts:
            counts[number] = 1
        elif number in counts:
            counts[number] += 1

    key = high = 0
    for num, cnt in counts.items():
        if cnt >= high:
            high = cnt
            if num > key:
                key = num
    print('#{} {} {}'.format(idx+1, key, high))
