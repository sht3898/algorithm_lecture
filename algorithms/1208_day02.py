for t in range(10):
    count = int(input())
    n = []
    for x in input().split():
        n.append(int(x))
    while count > 0:
        n[n.index(max(n))] -= 1
        n[n.index(min(n))] += 1
        count -= 1
    print('#{} {}'.format(t+1, n[n.index(max(n))] - n[n.index(min(n))]))