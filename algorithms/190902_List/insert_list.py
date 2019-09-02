arr = [69, 10, 30, 2, 16, 8, 31, 22]

N = len(arr)
# 삽입하는 작업을 n-1번 반복(1번 ~ n-1번)

for i in range(1, N):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > tmp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(arr)