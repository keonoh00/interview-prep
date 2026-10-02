# Flood Fill — Easy (#733)
# https://leetcode.com/problems/flood-fill/

r"""
An image is an m x n grid of integers, where image[i][j] is the colour of a pixel.
You are also given sr, sc and color. Starting from pixel image[sr][sc], recolour it
and every pixel connected to it (up, down, left or right) that has the same
original colour as the starting pixel, spreading outward the same way. Set all of
those pixels to color, and return the changed image.

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: Every 1 connected to the centre becomes 2. The bottom-right 1 is
    not connected to it (only diagonally), so it stays 1.

Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel already has colour 0, so nothing changes.

Constraints:
  - m == image.length
  - n == image[i].length
  - 1 <= m, n <= 50
  - 0 <= image[i][j], color < 2^16
  - 0 <= sr < m
  - 0 <= sc < n"""


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        raise NotImplementedError


CASES = [
    (([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    (([[0, 0, 0], [0, 0, 0]], 0, 0, 0), [[0, 0, 0], [0, 0, 0]]),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().floodFill, CASES)
