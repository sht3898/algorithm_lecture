import sys; sys.stdin = open('5110_input.txt', 'r')


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head is None:
            print('빈리스트')
            return

        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def findIdx(self, data):
        if self.head is None: # 빈 리스트
            return 0

        cur, idx = self.head, 0
        while cur is not None:
            if cur.data <= data:
                cur = cur.next
                idx += 1
            else:
                return idx

        if cur is None:
            return idx

        if self.head == cur:
            return 0

    def insertLast(self, node):
        if self.head is None: # 빈 리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertAt(self, idx, other):
        if self.head is None: # 빈리스트
            self.head = other.head
            self.tail = other.tail
            return

        prev, cur = None, self.head
        while idx > 0 and cur is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None: # 첫번째 위치에 삽입
            other.tail.next = cur
            self.head = other.head
        elif cur is None: # 마지막 위치에 삽입
            prev.next = other.head
            self.tail = other.tail
        else:
            prev.next = other.head
            other.tail.next = cur


    def printListReverse(self):
        if self.head is None:  # 빈리스트
            print('빈리스트')
            return

        cur, tmp = self.head, []
        while cur is not None:
            tmp.append(cur.data)
            cur = cur.next

        result = list(reversed(tmp))
        print(' '.join(list(map(str, result[:10]))))


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    mylist = LinkedList()

    for _ in range(M):
        inputs = list(map(int, input().split()))
        pos = mylist.findIdx(inputs[0])
        tmpList = LinkedList()
        for i in range(N):
            tmpList.insertLast(Node(inputs[i]))
        mylist.insertAt(pos, tmpList)

    print('#{}'.format(TC), end=' ')
    mylist.printListReverse()
