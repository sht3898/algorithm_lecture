from LinkedList import List, Node
print('03.insertfirst()_____________\n')

# ------------------------------------------------

mylist = List()
mylist.printlist()

mylist.insertfirst(Node(1))
mylist.insertfirst(Node(2))
mylist.insertfirst(Node(3))

mylist.printlist()

mylist.insertfirst(Node(4))
mylist.insertfirst(Node(5))

mylist.printlist()
