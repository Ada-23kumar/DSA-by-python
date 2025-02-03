class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.next = next
        self.item = item
        self.prev = prev

class DLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start (self, data):
        new_node = Node(None, data, self.start)
        if not self.is_empty():
            self.start = new_node
        else:
            self.start = new_node

    def insert_at_last(self, data):
        temp = self.start
        if self.start !=None:
            while temp.next != None:
                temp = temp.next

        new_node = Node(temp, data, None)
        if temp == None:
            temp = new_node
        else:
            temp.next = new_node

    def print_list(self):
        temp = self.start

        while temp is not None:
            print(temp.item, end = " ")
            temp = temp.next
         
    def search(self, data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp != None:
            new_node = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = new_node
        temp.next = new_node

    def delete_at_start(self):
        if self.start is None:
            self.start = self.start.next
            # return
            if self.start is not None:
                self.start.prev = None
        # else:
            # self.start = self.start.next
            

    def delete_at_end(self):
        if self.start is None:
            pass
        elif self.start.next is None:
        # temp = self.start
            self.start = None
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None


    def delete_item (self, data):
        if self.start is None:
            pass
        else:
            temp = self.start 
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:

                        temp.next.prev = temp.next.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next


    def __iter__(self):
        return DLLiterator(self.start)
    
class DLLiterator:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
        # else:


        


# dLL = DLL()
# # dLL.insert_at_start(10)
# # dLL.insert_at_start(20)
# # dLL.insert_at_start(30)
# DLL.insert_at_last(40)
# DLL.insert_at_last(50) 
# dLL.print_list()  # Output: 30 20 10 50 40

my_list = DLL()
my_list.insert_at_start(10)
my_list.insert_at_start(15)
my_list.insert_at_last(20)
my_list.insert_at_last(30)

my_list.insert_after(my_list.search(10),30)

for x in my_list:
    print(x, end = " ")

print()

