#making a custom queue class
class Queue():
    def __init__(self) -> None:
        self.q = []
    def enqueue(self, num):
        self.q.append(num)
    def dequeue(self):
        return self.q.pop(0)
    def is_empty(self):
        if len(self.q) == 0:
            return True

#making push costly approach
class StackFromQueue():
    def __init__(self) -> None:
        self.s = Queue()
        self.temp = Queue()
    def __str__(self) -> str:
        value = []
        
        return 
    def push(self, num):
        self.temp.enqueue(num)
        while not self.s.is_empty():
            self.temp.enqueue(self.s.dequeue())
        self.s, self.temp = self.temp, self.s
    def pop(self):
        return self.s.dequeue()

s1 = StackFromQueue()
s1.push(3)
s1.push(7)
s1.push(18)
