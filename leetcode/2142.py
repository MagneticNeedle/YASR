# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
class Solution:
    def checkString(self, s: str) -> bool:
        return not "ba" in s