import sys; sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())        # 노드수, 간선수
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[arr[i]] == 0: L[p] = c
    else: R[p] = c
    P[c] = p        # 부모 정보는 필요한 경우에 저장해서 사용


# -----------------------------------------------
def inorder(v):     # v = 현재 노드
    if v == 0: return
    print(v, end=' ')
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])
    print(v, end=' ')


# -----------------------------------------------
def inorder2(v):     # v = 현재 노드
    if L[v]:
        inorder2(L[v])
    print(v, end=' ')
    if R[v]:
        inorder2(R[v])

# -----------------------------------------------
# inorder(1)


# inorder2(1)
# print()


# 1. 트리 순회(전위, 중위, 후위)
# 전위
def preorder(v):
    print(v, end=' ')
    if L[v]:
        preorder(L[v])
    if R[v]:
        preorder(R[v])


print('전위 순회')
preorder(1)
print()


# 중위
def in_order(v):     # v = 현재 노드
    if L[v]:
        in_order(L[v])
    print(v, end=' ')
    if R[v]:
        in_order(R[v])


print('중위 순회')
in_order(1)
print()


# 후위
def postorder(v):
    if L[v]:
        postorder(L[v])
    if R[v]:
        postorder(R[v])
    print(v, end=' ')


print('후위 순회')
postorder(1)
print()

# 2. 트리의 높이, treeHeight(v): v를 루트로 하는 트리의 높이 계산
def tree_height(v):
    if v == 0:
        pass

# 3. 높이가 3인 노드들을 찾아서 출력하시오
# 4. 트리의 노드 수, treeSize(v): v를 루트로 하는 트리의 노드수 계산
# 5. 9번 노드의 조상을 찾고, 13번 노드의 조상 찾고, 두 노드의 공통 조상 찾기
