arr = 'algorithm'
arr = list(arr)
print(arr)
N = len(arr)
for i in range(N//2):
    arr[i], arr[N - 1 - i] = arr[N - 1 - i], arr[i]
print(arr)
