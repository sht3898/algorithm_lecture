from LinkedList import List, Node
print('01.printlist()_____________\n')

# ------------------------------------------------

mylist = List()
n1 = Node(1); n2 = Node(2);
n3 = Node(3); n4 = Node(4);
n5 = Node(5);

mylist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
mylist.size = 5
mylist.printlist()
