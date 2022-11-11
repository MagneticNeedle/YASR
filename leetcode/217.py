# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

print(Solution().containsDuplicate([1,2,3,4]))