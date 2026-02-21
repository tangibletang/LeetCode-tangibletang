from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        #rotate the queue: 
        for i in range(len(self.queue)-1):
            #pop the front value and add it to the end of the queue
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        #top is already the front
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()