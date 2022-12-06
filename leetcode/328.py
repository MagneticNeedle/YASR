from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head:
            odd,even,eh = head, head.next, head.next

            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next

            odd.next = eh
        return head

