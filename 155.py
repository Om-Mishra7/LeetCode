class MinStack():

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val):
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self):
        if self.stack.pop() == self.min[-1]:
            del self.min[-1]
        print(self.stack)
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min[-1]
        
    
minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())