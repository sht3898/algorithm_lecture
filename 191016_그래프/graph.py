import sys; sys.stdin = open('graph.txt', 'r')

V, E = map(int, input().split())        # 정점수, 간선수
Edge = [tuple(map(int, input().split())) for _ in range(E)]  # (u, v, w)
p = [x for x in range(V+1)]     # 부모


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

print(Edge)
Edge.sort(key=lambda x: x[2])
print(Edge)
MST = []
idx = 0
while len(MST) < V - 1:
    u, v, w = Edge[idx]
    a = find_set(u); b = find_set(v)
    if a != b:
        MST.append((u, v, w))
        p[b] = a
    idx += 1
print(MST)