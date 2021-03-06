
'''
Solution using minHeap: 
addItem(): O(Nlog N) time where N is the total number of items that arrive and can be inside the window 
getResult(): O(1) time
size(): O(1) time
O(N) space for storing the heap
- I am still thinking if it is possible to reduce more the time 
'''
from heapq import *
class SlideSumBasic:
    def __init__(self, window):
        self.current_sum = 0 
        self.window = window
        self.myheap = []

    def getResult(self):
        return self.current_sum

    def size(self):
        return len(self.window)

    def addItem(self, ts, value):
        self.current_sum += value
        heappush( self.myheap, (ts, value) )
        while len(self.myheap)>0 and self.myheap[0][0] <= ts - self.window :
            cur = heappop(self.myheap)
            self.current_sum -= cur[1]

#Test cases
slide = SlideSumBasic(50)   
slide.addItem(0,10)
slide.addItem(30,2)
slide.addItem(45,1)
print(slide.getResult())
slide.addItem(55,1)
print(slide.getResult())


