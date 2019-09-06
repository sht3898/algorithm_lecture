from queue import PriorityQueue

arr = [(3, 2), (2, 5), (1, 8), (0, 9), (2, 1), (3, 4), (2, 1)]

PQ = PriorityQueue
for val in arr:
    PQ.put(val)

while not PQ.empty():
    print(PQ.get())