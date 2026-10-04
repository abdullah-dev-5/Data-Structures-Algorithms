class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# Creating initial linked list

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head of linked list
head = node1



# Insert at beginning

new_node = Node(60)
new_node.next = head
head = new_node



# Insert at end

new_node2 = Node(100)

current = head
while current.next is not None:
    current = current.next

current.next = new_node2



# Insert after node with value 20

new_node3 = Node(70)

current = head

# Traverse until we find value ou20
while current is not None and current.data != 20:
    current = current.next

# Insert only if node exists
if current is not None:

    new_node3.next = current.next
    current.next = new_node3



# Traversing linked list

current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")







