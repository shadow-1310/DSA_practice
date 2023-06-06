# correct solution. done on 06-06-2023
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]


minStack =  MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()       # return 0
minStack.getMin() # return -2

