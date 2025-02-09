from singly_linked_list import *

class stack(SLL):

    def isEmpty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_start(data)

    def pop(self):
        if not self.isEmpty():
            self.delete_at_start()
