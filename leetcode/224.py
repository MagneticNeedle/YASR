# https://leetcode.com/problems/basic-calculator/

"""
Classic stack problem :)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans, curr, sign = 0, 0, 1
        for i in s:
            if i == " ":
                continue
            if i.isdigit():
                curr = curr*10 + int(i)
            elif i == "+":
                ans += curr * sign
                curr = 0
                sign = 1
            elif i == "-":
                ans += curr * sign
                curr = 0
                sign = -1
            elif i == '(':
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            else:
                ans += curr * sign
                ans *= stack.pop()
                ans += stack.pop()
                curr = 0
        return ans + (curr * sign)

