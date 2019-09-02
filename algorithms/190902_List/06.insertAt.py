from LinkedList import List, Node
print('06.inserrtAt()_____________\n')
# ------------------------------------------------

mylist = List()
for i in range(1, 6):
    mylist.insertlast(Node(i))

mylist.printlist()

mylist.insertAt(2, Node(100))
mylist.insertAt(4, Node(200))
mylist.printlist()

mylist.insertAt(3, Node(-1))
mylist.insertAt(10, Node(-2))
mylist.printlist()
