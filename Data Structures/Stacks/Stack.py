class Stack:
    def __init__(self, size: int) -> None:
        self.max_size = size
        self.stack = [None] * size
        self.top = -1

    # Push value onto stack
    def push(self, value):
        if self.top == self.max_size - 1:
            print(f"[OVERFLOW] Cannot push {value}, stack is full!")
            return
        self.top += 1
        self.stack[self.top] = value
        print(f"[PUSH] {value} added to stack at index {self.top}.")

    # Pop value from stack
    def pop(self):
        if self.top == -1:
            print("[UNDERFLOW] Cannot pop, stack is empty!")
            return None
        popped = self.stack[self.top]
        self.stack[self.top] = None
        print(f"[POP] {popped} removed from index {self.top}.")
        self.top -= 1
        return popped

    # Peek at the top element
    def peek(self):
        if self.top == -1:
            print("[PEEK] Stack is empty!")
            return None
        print(f"[PEEK] Top element: {self.stack[self.top]} at index {self.top}.")
        return self.stack[self.top]

    # Check if stack is empty
    def is_empty(self):
        if self.top == -1:
            print("[CHECK] Stack is empty.")
            return True
        else:
            print("[CHECK] Stack is not empty.")
            return False

    # Check if stack is full
    def is_full(self):
        if self.top == self.max_size - 1:
            print("[CHECK] Stack is full.")
            return True
        else:
            print("[CHECK] Stack is not full.")
            return False

    # Display the stack nicely
    def stack_view(self):
        if self.top == -1:
            print("[STACK VIEW] Stack is empty!")
            return
        print("\n=== STACK VIEW ===")
        print("TOP")
        for i in range(self.top, -1, -1):
            print(f"| {self.stack[i]} |")
        print("BOTTOM\n")


# ----------------- Testing -----------------
nums = Stack(10)

nums.is_empty()
nums.push(0)
nums.push(6)
nums.push(4)
nums.push(7)
nums.push(34)
nums.push(64)
nums.push(35)
nums.push(23)
nums.stack_view()
nums.pop()
nums.stack_view()
nums.peek()
nums.pop()
nums.push(35)
nums.push(35)
nums.push(35)
nums.is_full()
nums.stack_view()

