class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def isEmpty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.isEmpty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.start.item
        else:
            raise self.isEmpty()

    def size(self):
           return self.item_count
    
    def Display(self):
        if not self.isEmpty():
            temp = self.start
            while temp.next != None:
                print(temp.item, end=", ")
                temp = temp.next
            if temp.next == None:
                print(temp.item)
        else:
            return print("zero element in stack")

s1 = stack()
s1.push(23)
s1.push(12)
s1.push(123)
s1.push(231)
# print(s1.pop())
# print(s1.peek())
# print(s1.size())
s1.Display()