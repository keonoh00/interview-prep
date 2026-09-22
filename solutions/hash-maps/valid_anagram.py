# Valid Anagram — Easy (#242)
# https://leetcode.com/problems/valid-anagram/
# Day 1 · Tue 22 Sep
# not yet attempted

r"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
1 Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

Tags: hash-table, string, sorting"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        raise NotImplementedError

CASES = [
    (('anagram', 'nagaram'), True),
    (('rat', 'car'), False),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().isAnagram, CASES)
