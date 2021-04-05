"""
queue: a fixed size array to hold the elements for the circular queue.
headIndex: an integer which indicates the current head element in the circular queue.
count: the current length of the circular queue, i.e. the number of elements in the circular queue. Together with the headIndex, we could locate the current tail element in the circular queue, based on the formula we gave previously. Therefore, we choose not to add another attribute for the index of tail.
capacity: the capacity of the circular queue, i.e. the maximum number of elements that can be hold in the queue. 


"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.capacity = k
        self.headIndex=0
        self.count=0
        
      
        

    def enQueue(self, value: int) -> bool:
        if self.count==self.capacity: return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True
        
        
        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True
        
        
        
        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]
       
        

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]
        
        

    def isEmpty(self) -> bool:
        return self.count == 0
       
        

    def isFull(self) -> bool:
        return self.count == self.capacity
       
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()