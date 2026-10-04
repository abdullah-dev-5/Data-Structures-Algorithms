class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            head = new_node
        else:   
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current  
    
    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_begining(data)
            return
        count = 0
        current = self.head
        while current and count < position - 1:
            current = current.next
            count += 1

        new_node.next = current.next 
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node
            current.next = new_node

    def list_Values(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current = current.next
        print(None)


dll = DoublyLinkedList()

dll.insert_at_begining(10)
dll.insert_at_begining(20)
dll.insert_at_begining(30)
dll.insert_at_begining(40)
dll.insert_at_begining(50)
dll.insert_at_end(20)
dll.insert_at_position(22,3)
dll.list_Values()