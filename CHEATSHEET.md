# Choosing a technique

Before writing code, take about two minutes and say three things out loud: the size
limit, the brute force and its big-O, and the technique you'll use.

## 1. Read the size limit

It tells you how fast you need to be. Python does roughly 10 million simple steps in
about a second.

| Limit | What fits | Example |
|---|---|---|
| n ≤ about 20 | trying every choice, O(2ⁿ) | |
| n ≤ about 3,000 | O(n²) | 3Sum: n² = 9 million is fine, n³ = 27 billion isn't |
| n up to 10⁵ or 10⁶ | O(n) or O(n log n) | Longest Substring Without Repeating Characters |
| the answer can be up to 10⁹ | binary search on the answer, about 30 tries | Koko Eating Bananas |

## 2. Say the brute force, then ask what it repeats

The technique is whatever stops the repeat.

- **3Sum:** three loops check every triplet. After sorting, one sum that's too small
  rules out a whole row of pairs, so you get two pointers.
- **Longest Substring Without Repeating Characters:** brute force restarts from every
  starting letter. Keep the window and only drop from the front, so you get a sliding
  window.
- **Koko Eating Bananas:** trying speeds 1, 2, 3, … one by one wastes time. "Too slow"
  rules out every slower speed too, so you get binary search.

## 3. Match the wording to a technique

| If the problem says… | Try | Problems here |
|---|---|---|
| sorted array, or pairs/triplets adding up to a target | two pointers | Two Sum II, 3Sum, Container With Most Water |
| seen before? count? group? | hash map or set | Contains Duplicate, Group Anagrams, Top K Frequent Elements |
| a contiguous subarray whose sum is k | running total + hash map | Subarray Sum Equals K |
| longest/shortest *contiguous* piece that follows a rule | sliding window | Longest Substring Without Repeating Characters, Best Time to Buy and Sell Stock |
| sorted, or "smallest X that works" where checking one X is easy | binary search | Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko Eating Bananas |
| next greater/warmer, matching brackets | stack | Daily Temperatures, Valid Parentheses |
| k largest/smallest/closest | heap | Kth Largest Element in an Array, K Closest Points to Origin |
| grid regions, something spreading, fewest steps | DFS / BFS | Number of Islands, Rotting Oranges |
| tree | recursion on left and right, or BFS for levels | Validate Binary Search Tree, Binary Tree Level Order Traversal |
| overlapping intervals | sort by start, then merge | Merge Intervals |
| number of ways, or best total where each choice depends on earlier ones | dynamic programming | Climbing Stairs, House Robber |
| linked list | dummy node, slow/fast pointers | Linked List Cycle, Remove Nth Node From End of List |
