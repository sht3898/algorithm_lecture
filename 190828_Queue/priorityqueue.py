from heapq import heappush, heappop

Q = []
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

for val in arr:
    heappush(Q, val)

while len(Q) > 0:
    print(heappop(Q))
print()