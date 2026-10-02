# Valid Palindrome II — Easy (#680)
# https://leetcode.com/problems/valid-palindrome-ii/

r"""
Given a string s, return true if s can be a palindrome after deleting at most one
character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: Delete the "c" (or the "b").

Example 3:
    Input: s = "abc"
    Output: false

Constraints:
  - 1 <= s.length <= 10^5
  - s consists of lowercase English letters."""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        raise NotImplementedError


CASES = [
    (("aba",), True),
    (("abca",), True),
    (("abc",), False),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().validPalindrome, CASES)
