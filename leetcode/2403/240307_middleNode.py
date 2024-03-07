# https://leetcode.com/problems/middle-of-the-linked-list/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        maps = {}
        while head:
            maps[index] = head
            head = head.next
            index += 1
        return maps[index // 2]
