import sys
sys.stdin = open('bingo.txt', 'r')

numbers = []
speaks = []
bingo = 0
result_list = [[0] * 5 for _ in range(5)]
result = []
speak_list = []

for idx in range(5):
    numbers.append(list(map(int, input().split())))
for idx in range(5):
    speaks.append(list(map(int, input().split())))

for speak in speaks:
    for word in speak:
        speak_list.append(word)

for speak in speak_list:
    for idx in range(5):
        for idx2 in range(5):
            if speak == numbers[idx][idx2]:
                result.append([idx, idx2])

for couple in result:
    count = 0
    result_list[couple[0]][couple[1]] = 1
    for idx in range(5):
        if sum(result_list[idx]) == 5:
            bingo += 1
        count += 1

    for idx in range(5):
        same_list = []
        for idx2 in range(5):
            if idx+idx2 == 4:
                same_list.append(numbers[idx][idx2])
        if sum(same_list) == 5:
            bingo += 1
        count += 1

    for idx in range(5):
        height_list = []
        for idx2 in range(5):
            height_list.append(numbers[idx2][idx])
        if sum(height_list) == 5:
            bingo += 1
        count += 1

    if bingo == 3:
        print(count)
