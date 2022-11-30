from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf


class Solution:
    def search(self, nums: List[int], target: int, start=0, end=0, depth=0) -> int:
        if not nums:
            return -1
        if (n := len(nums)) == 1:
            if nums[0] == target:
                return start+1
            else:
                return -1
        mid = (n // 2)
        print(("\t"*depth) + f"{mid} {nums[mid]}")
        if target == nums[mid]:
            return mid + start
        if target > nums[mid]:
            print(("\t\t" * depth) + f"target in right")
            return mid-1 + self.search(nums[mid+1:n], target, mid+1, n-1)
        else:
            print(("\t\t" * depth) + f"target in left")
            return self.search(nums[0: mid], target, 0, mid)
