import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Array index out of range")

        return self.array[index]

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print(arr)
print("Size:", arr.size)
print("Capacity:", arr.capacity)