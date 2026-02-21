class MinStack:

    def __init__(self):
        self.stack1 = []
        self.min_element = []
        

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.min_element:
            self.min_element.append(val)
        else:
            if val < self.min_element[-1]: 
                self.min_element.append(val)
            else: 
                self.min_element.append(self.min_element[-1])
        

    def pop(self) -> None:
        self.stack1.pop()
        self.min_element.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.min_element[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()