class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        #outstack is the output

    def pop(self) -> int:
        
        if self.out_stack: 
            return self.out_stack.pop()
        else: 
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()

    def peek(self) -> int:
        #if outstack has items, return the last item. Becasue when you reversed it, in a queue you want the first item
        if self.out_stack: 
            return self.out_stack[-1]
        else: 
            #move eveyrthing to the outstack if it is empty. 
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]

    
    def empty(self) -> bool:
        if not self.out_stack and not self.in_stack:
            return True
        else: 
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()