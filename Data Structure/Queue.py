class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        self.items.append(data)

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            return None

        return self.items.pop(self.front)

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            return None

        return self.items[self.front]

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)

    def manual_size(self):
        """Calculate the queue size manually."""
        count = 0

        for _ in self.items:
            count += 1

        return count

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def show_values(self):
        """Display all elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return

        print(" - ".join(map(str, self.items)))


queue = Queue()

queue.enqueue(7)
queue.enqueue(5)
queue.enqueue(1)
queue.enqueue(8)
queue.enqueue(6)

queue.dequeue()
queue.dequeue()
queue.dequeue()

print("Front:", queue.peek())
print("Queue:", end=" ")
queue.show_values()

print("Manual size:", queue.manual_size())
print("Size:", queue.size())
