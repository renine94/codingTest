# https://leetcode.com/problems/remove-nodes-from-linked-list/description/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<ListNode val={self.val} next={self.next}>"


#################################################################################
# 내 풀이
#################################################################################
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        q = []

        while head:
            q.append(head.val)
            head = head.next

        while q:
            max_val = max(q)
            val = q.pop(0)
            if val == max_val:
                curr.next = ListNode(val)
                curr = curr.next
                q = list(filter(lambda x: x != max_val, q))
        return dummy.next


#################################################################################
# 다른사람 풀이 (정답)
#################################################################################
class Solution2:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        # Add nodes to the stack
        while current:
            stack.append(current)
            current = current.next

        current = stack.pop()
        maximum = current.val
        result_list = ListNode(maximum)

        # Remove nodes from the stack and add to result
        while stack:
            current = stack.pop()
            # Current should not be added to the result
            if current.val < maximum:
                continue
            # Add new node with current's value to front of the result
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val

        return result_list


head = ListNode(
    val=5, next=ListNode(val=2, next=ListNode(val=13, next=ListNode(val=3, next=ListNode(val=8, next=None))))
)
expected = ListNode(val=13, next=ListNode(val=8, next=None))
result = Solution().removeNodes(head)
assert result == expected
