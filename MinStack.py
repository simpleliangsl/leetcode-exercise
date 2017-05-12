class MinStack:
    def __init__(self):
        self.elementStack = []
        self.minStack = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.elementStack.append(x)
        if x <= self.minStack[-1]:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        x = self.elementStack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()

    # @return an integer
    def top(self):
        return self.elementStack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1]
