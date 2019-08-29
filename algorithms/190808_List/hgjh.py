a = 'ABCD'
n = len(a)
for i in range(1<<n):
    result = []
    result2 = []
    for j in range(n):
        if i & (1 << j):
            result.append(a[j])
        else:
            result2.append(a[j])
    if len(result) == 2:
        print(result, result2)
