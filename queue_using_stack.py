class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbound=[]
        self.outbound=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbound.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outbound) == 0:
            while self.inbound:
                self.outbound.append(self.inbound.pop())
        return self.outbound.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outbound) == 0:
            return self.inbound[0]
        else:
            return self.outbound[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inbound and not self.outbound 

queue =  MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())   # returns 1
queue.pop()   # returns 1
print(queue.empty()) #returns false