class Node:

    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start = None):
        self.start = start

    def __str__(self):
        return "Hello everyone this is program for Singly linked list"
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node
        
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty() != None:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node
    
    def search(self, data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node

    def print_list(self):
        temp = self.start

        while temp is not None:
            print(temp.item, end = " ")
            temp = temp.next


    def delete_at_start(self):
        # if not self.start:
        #     print("list is empty. No Node to Delete.")
        #     return 
        # self.start = self.start.next
        if self.start is not None:
            self.start = self.start.next


    def delete_at_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None 
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    def delete_at_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
            else:
                pass
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next

            else:

                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    
"""
my_SLL = SLL()

print(my_SLL)
search = my_SLL.search(23)
print(search)
    
my_SLL.insert_at_start(23)
my_SLL.insert_after(my_SLL.search(23), 12)
my_SLL.insert_at_end(34)
# my_SLL.print_list()
# my_SLL.delete_at_start()
my_SLL.insert_after(my_SLL.search(34), 23)
my_SLL.print_list()
print("\n")
# my_SLL.delete_at_end()
my_SLL.delete_at_item(12)
my_SLL.print_list()
print('\n')
# print(ls)
"""