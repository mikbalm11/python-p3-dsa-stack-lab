class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for item in items:
            if(not self.full()):
                self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if (self.full()):
            return None
        else:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        itemslength = len(self.items)
        for i in range(itemslength):
            if self.items[i] == target:
                return itemslength - (i + 1)
        return -1
