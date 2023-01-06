#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # sort and the choose till no coins left

        return sum(1 for i in sorted(costs)if(coins:=coins-i)>=0)

        
# @lc code=end

