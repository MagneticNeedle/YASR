# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [_ for _ in bank if "1" in _] # we only care for rows that contain devices
        nb = 0
        for i,r in enumerate(bank):
            if (n:=i+1)<len(bank):
                nb += r.count('1') * bank[n].count('1')  # just do a product :) 
        return nb
