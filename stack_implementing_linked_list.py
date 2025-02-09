from singly_linked_list import *

class stack:
    def __init__(self):
        self.MySll = SLL()
        self.item_count = 0
    
    def isEmpty(self):
        return self.MySll.is_empty()
    
    def push(self, data):
        self.MySll.insert_at_start(data)
        self.item_count += 1
    
    def pop(self):
        if not self.isEmpty():
            data = self.MySll.start.item
            self.MySll.delete_at_start()
            self.item_count -= 1
            return data

    def peek(self):
        if  not self.isEmpty():
           return self.MySll.start.item
    
    def size(self):
        return self.item_count
    

s = stack()
s.push(2)
s.push(3)
s.push(23)
print(s.peek())

print(s.pop())
print(s.size())
print(s.peek())