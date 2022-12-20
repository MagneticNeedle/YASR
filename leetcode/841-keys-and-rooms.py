from typing import List
from collections import defaultdict
#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_map = set([0])
        stack = []
        stack.extend(rooms[0])
        while stack:
            room = stack.pop()
            if room not in room_map:
                room_map.add(room)
                stack.extend(rooms[room])
        return len(room_map) == len(rooms)

        
# @lc code=end

