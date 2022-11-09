# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = list(map(int, filter(str.isnumeric, s.split())))
        return all(x<y for x,y in zip(l,l[1:]))

