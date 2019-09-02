class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # def __del__(self):
    #     print(self.data, '삭제')


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        result = []
        if self.head is None:       # 공백 리스트인지 체크
            return

        cur = self.head
        # print('[ ', end='')
        # while cur is not None:
        #     print(cur.data, end=' ')
        #     cur = cur.next
        # print(']')
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        print(*result)

    def insertlast(self, node):
        if self.head is None:       # 빈 리스트
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None:
            return
        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur              # 이전 노드를 백업
            cur = cur.next

        if prev is None:            # if self.size == 1 노드가 1개일 때,
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev

        del cur
        self.size -= 1

    def deletefirst(self):
        if self.head is None:
            return

        cur = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = cur.next

        del cur
        self.size -= 1

    def insertAt(self, idx, node):      # idx: 삽입 위치, node: 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:            # 1위치에 삽입
                node.next = cur
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
            else:                       # 범위 벗어나 마지막 위치에 삽입
                node.next = cur
                prev.next = node
        self.size += 1

    def deleteAt(self, idx):
        if self.head is None:
            return
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:
                self.head = self.tail = None
            elif cur is None:
                prev.next = None
                self.tail = prev
            else:
                prev.next = cur.next

        del cur
        self.size -= 1
