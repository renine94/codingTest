# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
import sys
from typing import Optional
from decimal import Decimal

sys.set_int_max_str_digits(0)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<ListNode val={self.val} next={self.next}>"


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        double = list(map(str, values))
        double_value = list(str(int("".join(double)) * 2))
        # double_value2 = list(str(Decimal("".join(double)) * 2))

        dummy = ListNode(0)

        first_value = double_value.pop(0)
        current = ListNode(val=first_value)

        dummy.next = current

        for v in double_value:
            node = ListNode(v)
            current.next = node
            current = node

        return dummy.next


head = ListNode(val=1, next=ListNode(val=8, next=ListNode(val=9, next=None)))
expected = ListNode(val=3, next=ListNode(val=7, next=ListNode(val=8, next=None)))

result = Solution().doubleIt(head)
assert result == expected
