# https://leetcode.com/problems/maximum-subarray/
from math import inf
class Solution:
    def maxSubArray(self, nums: list[int], left=None, right=None) -> int:
        # basic method
        # cur_sum = 0
        # max_sum = -inf
        # for i in nums:
        #     cur_sum += i
        #     if cur_sum > max_sum:
        #         max_sum = cur_sum
        #     if cur_sum < 0:
        #         cur_sum = 0
        # return max_sum

        # recursive
        if not nums:
            return 0
        
        if left is None and right is None:
            left, right = 0, len(nums)-1
        
        if left == right: # only one element
            return nums[left]

        mid = (left + right) // 2

        leftMax = -inf
        t = 0
        for i in range(mid, left-1, -1):
            t += nums[i]
            if t > leftMax:
                leftMax = t
        rightMax = -inf
        t = 0
        for i in range(mid+1, right+1):
            t += nums[i]
            if t > rightMax:
                rightMax = t
        
        maxSub = max(self.maxSubArray(nums, left, mid), self.maxSubArray(nums, mid+1, right))

        return max(maxSub, leftMax+rightMax)

# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



