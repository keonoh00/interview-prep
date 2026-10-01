# Choosing a technique

Before writing code, take about two minutes and say three things out loud:

1. **The size limit:** how fast do I need to be?
2. **The brute force:** what does it keep repeating?
3. **The clue in the wording:** which technique does it point to?

---

## Step 1: How fast do I need to be?

Look at n in the problem's constraints. Python does about 10 million simple steps a
second.

| n is up to | Aim for |
|---|---|
| 20 | O(2ⁿ), so trying every choice is fine |
| 3,000 | O(n²) |
| 100,000 or more | O(n) or O(n log n) |

If the **answer** itself can be as big as 10⁹, think binary search on the answer.
That's only about 30 tries.

---

## Step 2: What does the brute force repeat?

Say the brute force first. Then ask what work it keeps doing again. The technique is
whatever removes that repeat.

| Problem | Brute force | Better |
|---|---|---|
| 3Sum | checks every triplet, O(n³) | sort, then two pointers: one sum rules out a whole row, O(n²) |
| Longest Substring | restarts from every letter | sliding window: keep the window, drop from the front, O(n) |
| Koko Eating Bananas | tries speeds 1, 2, 3, … | binary search: "too slow" rules out every slower speed too |

---

## Step 3: Which technique does the wording point to?

### Two pointers
- **Clue:** a sorted array; a pair or triplet that adds up to a target
- **How:** start at both ends. If the sum is too small, move the left pointer right.
  If it's too big, move the right pointer left.
- **Done:** Two Sum II, 3Sum, Container With Most Water

### Hash map or set
- **Clue:** "seen this before?", counting, grouping
- **How:** store what you've seen, so each lookup is O(1)
- **Done:** Contains Duplicate, Group Anagrams, Top K Frequent Elements

### Running total + hash map
- **Clue:** a contiguous subarray whose sum is k
- **How:** the sum from i to j is the total at j minus the total before i, so look up
  `total - k` in the map
- **Done:** Subarray Sum Equals K

### Sliding window
- **Clue:** the longest or shortest *contiguous* substring or subarray that follows
  a rule
- **How:** grow the right end. When the rule breaks, shrink from the left until it
  holds again.
- **Done:** Longest Substring Without Repeating Characters, Best Time to Buy and Sell
  Stock

### Binary search
- **Clue:** sorted input, or "the smallest X that works" where checking one X is easy
- **How:** check the middle and throw away the half that can't hold the answer
- **Done:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko Eating
  Bananas

### Stack
- **Clue:** the next greater or warmer item; matching brackets
- **How:** keep the items still waiting for an answer, and pop each one when its
  answer arrives
- **Done:** Daily Temperatures, Valid Parentheses

### Heap
- **Clue:** the k largest, smallest or closest
- **How:** keep a heap of size k (`heapq` is a min-heap)
- **Done:** Kth Largest Element in an Array, K Closest Points to Origin

### DFS or BFS
- **Clue:** regions in a grid, something spreading, the fewest steps
- **How:** visit a cell, mark it, then visit its neighbours. Use BFS (a queue) when
  you need the fewest steps.
- **Done:** Number of Islands, Rotting Oranges

### Tree recursion
- **Clue:** any binary tree
- **How:** solve for the left and right subtrees, then combine them. For level by
  level, use BFS with a queue.
- **Done:** Validate Binary Search Tree, Binary Tree Level Order Traversal

### Sort, then merge
- **Clue:** overlapping intervals
- **How:** sort by start. If the next interval starts before the current one ends,
  merge them.
- **Done:** Merge Intervals

### Dynamic programming
- **Clue:** the number of ways, or the best total where each choice depends on earlier
  ones
- **How:** build the answer for i from the answers for i - 1 and i - 2
- **Done:** Climbing Stairs, House Robber

### Linked list tricks
- **Clue:** any linked list
- **How:** a dummy node saves special cases for the head. For slow and fast pointers,
  fast moves 2 steps and slow moves 1.
- **Done:** Linked List Cycle, Remove Nth Node From End of List
