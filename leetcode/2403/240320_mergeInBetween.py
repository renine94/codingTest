# https://leetcode.com/problems/merge-in-between-linked-lists/

import copy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    링크드 리스트에서 a, b 구간 제거하고 list2 랑 합치기...
    (거지같이 풀었음 ㅠ)
    """

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def find_node_by_index(array: ListNode, index: int):
            for _ in range(index - 1):
                array = getattr(array, "next")
            return array

        first_node = find_node_by_index(list1, a)
        second_node = find_node_by_index(list1, b + 2)

        first_node.next = list2

        i = 0
        temp = copy.deepcopy(list2)
        while True:
            temp = getattr(temp, "next")
            if temp is None:
                break
            i += 1

        for _ in range(i):
            list2 = getattr(list2, "next")

        list2.next = second_node

        return list1


############################################################################


# GPT3.5 에게 위 코드를 최적화 해달라고 했음
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Helper function to find the node by index
        def find_node_by_index(array: ListNode, index: int):
            for _ in range(index - 1):
                array = array.next
            return array

        # Find the nodes to merge between
        first_node = find_node_by_index(list1, a)
        second_node = find_node_by_index(list1, b + 1)

        # Connect the first list to the beginning of the second list
        first_node.next = list2

        # Find the end of the second list
        while list2.next:
            list2 = list2.next

        # Connect the end of the second list to the rest of the first list
        list2.next = second_node.next

        return list1
