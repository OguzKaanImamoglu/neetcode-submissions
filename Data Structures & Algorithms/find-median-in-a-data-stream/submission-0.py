
import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.left and self.right and -self.left[0]> self.right[0]:
            item = -heapq.heappop(self.left)
            heapq.heappush(self.right, item)

        if len(self.right)>len(self.left):
            item = heapq.heappop(self.right)
            heapq.heappush(self.left, -item)

        if len(self.left)>len(self.right)+1:
            item = -heapq.heappop(self.left)
            heapq.heappush(self.right, item)

        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2.0

        return -self.left[0]
        
        