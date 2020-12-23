class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack= []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.out_stack) == 0:

            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_stack:
            return self.in_stack[0]
        else:
            return self.out_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (len(self.in_stack)==0 and len(self.out_stack)==0)
 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()