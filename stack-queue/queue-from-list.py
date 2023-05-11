class Queue():
    def __init__(self) -> None:
        self.q = []
    def enqueue(self, num):
        self.q.append(num)
        print("new queue after operatio is: ", self.q)
    def dequeue(self):
        self.q.pop(0)
        print("new queue after operation is: ", self.q)
    def is_empty(self):
        if len(self.q) == 0:
            print("Yes")
        else:
            print("No")

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(9)
q.dequeue()
q.is_empty()
