class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

    def enQueue(self, item):
        global front, rear
        newNode = Node(item)
        if front == None:
            front = newNode
        else:
            rear.next = newNode
        rear = newNode

    def isEmpty(self):
        return front == None

    def deQueue(self):
        global front, rear
        if isEmpty():
            print('Queue_Empty')
            return None

        item = front.item
        front = front.next
        if front == None:
            rear = None
        return item

    def Qpeek(self):
        return front.item

    def printQ(self):
        f = front
        s = ''
        while f:
            s += f.item + ''
        return s


front = None
rear = None

enQueue('A')
enQueue('B')
enQueue('C')
printQ()
print(deQueue())
print(deQueue())
print(deQueue())