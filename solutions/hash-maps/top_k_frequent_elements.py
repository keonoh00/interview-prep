# Top K Frequent Elements — Medium (#347)
# https://leetcode.com/problems/top-k-frequent-elements/
# Day 1 · Tue 22 Sep
# not yet attempted

r"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Example 3:
    Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
    Output: [1,2]

Constraints:
1 Follow up: Your algorithm's time complexity must be better than O(n log n), where
n is the array's size.

Tags: array, hash-table, divide-and-conquer, sorting, heap-priority-queue, bucket-
      sort, counting, quickselect"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        raise NotImplementedError

CASES = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), [1, 2]),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().topKFrequent, CASES, any_order=True)
