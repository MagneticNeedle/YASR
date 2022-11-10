# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)
        return "".join(st)