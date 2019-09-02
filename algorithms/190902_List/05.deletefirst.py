from LinkedList import List, Node
print('05.deletefirst()_____________\n')

# ------------------------------------------------

mylist = List()
for i in range(1, 6):
    mylist.insertfirst(Node(i))

mylist.printlist()

mylist.deletefirst()
mylist.deletefirst()

mylist.printlist()

mylist.deletefirst()
mylist.deletefirst()
mylist.deletefirst()

mylist.printlist()
