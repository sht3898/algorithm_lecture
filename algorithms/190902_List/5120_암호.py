import sys; sys.stdin = open('5120_input.txt', 'r')
from LinkedList import Node, List

T = int(input())

for TC in range(1, T+1):
    N, M, K = map(int, input().split())     # N: 숫자 개수, M: 지정 위치로부터의 칸, K:반복횟수
    arr = list(map(int, input().split()))

    mylist = List()
    for i in range(N):
        mylist.insertlast(Node(arr[i]))
    mylist.printlist()
    for i in range(1, K+1):

        if 3*i < mylist.size+1:
            a = mylist.size + 1
            b = 3*i
            left, right = arr[3 * i - 1], arr[3 * i]
            node = Node(left + right)
            mylist.insertAt(3 * i, node)
        else:
            left, right = arr[(3*i) % N - 1], arr[(3*i) % N]
            node = Node(left + right)
            mylist.insertAt((3*i) % N, node)
    mylist.printlist()