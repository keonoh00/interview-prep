# Search a 2D Matrix — Medium (#74)
# https://leetcode.com/problems/search-a-2d-matrix/
# Day 4 · Fri 25 Sep
# not yet attempted

r"""
You are given an m x n integer matrix matrix with the following two properties:

  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the previous
    row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/10/05/mat.jpg]
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg]
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
  - m == matrix.length
  - n == matrix[i].length
  - 1 <= m, n <= 100
  - -10^4 <= matrix[i][j], target <= 10^4

Tags: array, binary-search, matrix"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        raise NotImplementedError

CASES = [
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().searchMatrix, CASES)
