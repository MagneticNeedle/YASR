from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (not list2):
            return list1 if list1 else list2 if list2 else None

        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)

        main_head = list1
        while True:
            if not list1.next:
                list1.next = list2
                break
            temp = list1.next
            if temp:
                while list2 and list2.val <= temp.val:
                    list1.next = list2
                    list2 = list2.next
                    list1 = list1.next
            list1.next = temp
            list1 = list1.next

        return main_head
