# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# in this we are abusing the fact that the array is sorted in ascending order
# so if it is ascending a smaller number cant come after a larger
# so this is impossible [1,2,1]
# we just need to check the last index :)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  
        n=len(nums)
        if n == 0 or n == 1:
            return n
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

        

nums = [1,1,2]
Solution().removeDuplicates(nums)
print(nums)