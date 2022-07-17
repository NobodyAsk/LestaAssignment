
class Fifo1():


    def __init__(self, num):
        self.num = num
        self.data = []
    

    def enqueue(self, value):
        if not self.is_full():
            self.data.append(value)
        else:
            print("Storage is full. Please, free some space with read_data function")
    

    def dequeue(self):
        if self.is_not_empty():
            return self.data.pop(0)
        else:
            print("No data")


    def is_not_empty(self):
        if self.size() != 0:
            return True
        else: 
            return False
    
    
    def size(self):
        return len(self.data)


    def is_full(self):
        if self.size() == self.num:
            return True
        else:
            return False


    def show_head(self):
        if self.is_not_empty():
            return self.data[len(self.data)-1]
        else:
            return "No data"


    def show_tail(self):
        if self.is_not_empty():
            return self.data[0]
        else:
            return "No data"


from collections import deque

class Fifo2():


    def __init__(self):
        self.queue = deque()


    def enqueue(self, x):
        return self.queue.appendleft(x)


    def dequeue(self):
        return self.queue.pop()

    
    def isEmpty(self):
        return len(self.queue) == 0


    def front(self):
        return self.queue[-1]


    def rear(self):
        return self.queue[0]
    

    def size(self):
        return len(self.queue)