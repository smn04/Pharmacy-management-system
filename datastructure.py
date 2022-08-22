class Stack:
    def __init__(self):
        self.data = []
        self.rear = -1
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self, element):
        self.data.insert(0,element)
        self.rear += 1
    def pop(self):
        if self.is_empty():
            raise ValueError('Cannot pop element from empty stack')
        else:
            self.rear -= 1
            return self.data.pop(0)
            