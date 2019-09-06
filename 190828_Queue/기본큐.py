def enQueue(item):
    queue.append(item)


def deQueue():
    if isEmpty():
        print('Queue_Empty')
    else:
        return queue.pop(0)


def isEmpty():
    return len(queue) == 0


def Qpeek():
    if isEmpty():
        print('Queue_Empty')
    else:
        return queue[0]


queue = []
# front: -1
# rear: len(queue)-1


enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())