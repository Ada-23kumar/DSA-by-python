class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next - next

class CDLL:
    def __init__(self, start = None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            self.start.prev.next = new_node
            self.start.prev = new_node

        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            new_node.prev.next = new_node
            self.start.prev = new_node

    def search(self, item):
        temp = self.start
        if temp.item == item:
            return temp
        else:
            temp = temp.next

        while temp != self.start:
            if temp.item == item:
                return temp
            temp = temp.next

        return None
    
    def insert_after(self, temp, data):
        if temp != None:
            new_node = Node(data)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
    
    def print_list(self):
        temp = self.start
        if temp == self.start:
            print(temp.item, end = ' ')
            temp = temp.next
            while temp != self.start:
                print(temp.item, end = ' ')
                temp = temp.next

    def delete_first(self):
        if self.start != None:
            if self.start.next == self.start:
                self.start = None

            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
                 
    def delete_at_last(self):
        if self.start != None:
            if self.start.next == self.start:
                self.start = None

            else:
                self.start.prev.prev.next = self.start
                self.start.preve = self.start.prev.prev


    def delete_item (self, data):
        if self.start is not None:
            if self.start.next == self.start and self.start.item == data:
                self.start = None
            else:
                
