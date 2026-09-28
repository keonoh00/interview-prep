# Merge Two Sorted Lists — Easy (#21)
# https://leetcode.com/problems/merge-two-sorted-lists/
# Day 7 · Mon 28 Sep
# not yet attempted

r"""
You're given the heads of two sorted linked lists, list1 and list2.

Merge them into one sorted list by linking together the nodes they already have,
and return the head of the merged list.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg]
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
  - The number of nodes in both lists is in the range [0, 50].
  - -100 <= Node.val <= 100
  - Both list1 and list2 are sorted in non-decreasing order.

Tags: linked-list, recursion"""

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        raise NotImplementedError

CASES = [
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([], []), []),
    (([], [0]), [0]),
]

if __name__ == "__main__":
    # ListNode too, so your code can call ListNode() just as it can on LeetCode.
    from interview_prep import run, ListNode, build_linked_list, linked_list_to_list

    def call(a, b):
        merged = Solution().mergeTwoLists(build_linked_list(a), build_linked_list(b))
        return linked_list_to_list(merged)

    run(call, CASES)
