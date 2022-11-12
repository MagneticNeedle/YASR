import bisect
class MedianFinder:

    def __init__(self):
        self.array = []
        self.mid = -1
        self.is_even = True

    def addNum(self, num: int) -> None:
        bisect.insort(self.array, num)
        if self.is_even:
            self.mid += 1
        self.is_even = not self.is_even

    def findMedian(self) -> float:
        if self.is_even:
            return (self.array[self.mid] + self.array[self.mid+1]) / 2
        return self.array[self.mid]
        


# Your MedianFinder object will be instantiated and called as such:
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
obj = MedianFinder()
functions = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
inputs = [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
functions = functions[1:]
inputs = inputs[1:]
for index, function in enumerate(functions):
    if function == "addNum":
        obj.addNum(inputs[index][0])
    elif function == "findMedian":

        print(f'mid:- {obj.mid}, {obj.findMedian()}, \t{obj.array}', end='\n')
