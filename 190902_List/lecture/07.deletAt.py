from LinkedList import List, Node
print('07.deleteAt()_____________\n')
# ------------------------------------------------

mylist = List()
for i in range(1, 6):
    mylist.insertfirst(Node(i))

mylist.printlist()

mylist.deleteAt(2)
mylist.deleteAt(4)

mylist.printlist()

mylist.deleteAt(3)
mylist.printlist()

