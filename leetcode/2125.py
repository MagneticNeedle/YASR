# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [_.count("1") for _ in bank if "1" in _]
        nb = 0
        for i,r in enumerate(bank):
            if (n:=i+1)<len(bank):
                nb += r * bank[n]
        return nb
