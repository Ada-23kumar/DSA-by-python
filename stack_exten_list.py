class Stak(list):
    def is_enmpty(self):
        return len(self) == 0
    
    def push(self, item):
        self.append(item)

    def pop(self): 
        if not self.is_enmpty():
            return super().pop()
        else:
            raise IndexError ("stack is empty")
        
    def  peak(self):
        if not self.is_enmpty():
            return self[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len(self)
    
    