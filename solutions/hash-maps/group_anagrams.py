# Group Anagrams — Medium (#49)
# https://leetcode.com/problems/group-anagrams/
# Day 1 · Tue 22 Sep
# not yet attempted

r"""
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Explanation: - There is no string in strs that can be rearranged to form "bat".
    - The strings "nat" and "tan" are anagrams as they can be rearranged to form each
    other.
    - The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
    form each other.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
  - 1 <= strs.length <= 10^4
  - 0 <= strs[i].length <= 100
  - strs[i] consists of lowercase English letters.

Tags: array, hash-table, string, sorting"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        raise NotImplementedError

CASES = [
    (
        (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],),
        [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']],
    ),
    (([''],), [['']]),
    ((['a'],), [['a']]),
]

if __name__ == "__main__":
    from interview_prep import run

    run(Solution().groupAnagrams, CASES, any_order=True)
