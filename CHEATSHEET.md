# Choosing a technique

Before writing code, take about two minutes and say three things out loud:

1. **The type and the constraints:** which algorithm fits?
2. **The brute force:** what does it keep repeating?
3. **The clue in the wording:** which technique does it point to?

---

## Step 1: What type of question, and how big is n?

Find the type on the left, then the row for your n. Inside each type, rows go from
slowest to fastest, so anything further down also works.

<table>
<tr><th>Type of question</th><th>Constraint</th><th>Time</th><th>Algorithm</th></tr>
<tr><td rowspan="16">Array or string</td><td>n ≤ 10</td><td>O(n!)</td><td>Backtracking: try every order (Permutations)</td></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>Backtracking: take it or skip it (Subsets)</td></tr>
<tr><td>n ≤ 200</td><td>O(n³)</td><td>Three nested loops: every triplet</td></tr>
<tr><td rowspan="4">n ≤ 3,000</td><td rowspan="4">O(n²)</td><td>Two nested loops: every pair</td></tr>
<tr><td>Sort, then two pointers for each item: triplets (3Sum)</td></tr>
<tr><td>DP that looks back at every j &lt; i: longest increasing subsequence, Word Break</td></tr>
<tr><td>DP on two strings: common subsequence, edit distance</td></tr>
<tr><td rowspan="8">n ≤ 10⁵</td><td>O(n log n)</td><td>Sort first</td></tr>
<tr><td>O(n log k)</td><td>Heap of size k: the k largest, smallest or closest</td></tr>
<tr><td rowspan="6">O(n)</td><td>Hash map or set: seen before, counting, grouping</td></tr>
<tr><td>Running total + hash map: a subarray whose sum is k</td></tr>
<tr><td>Two pointers: a pair in a sorted array, palindromes</td></tr>
<tr><td>Sliding window: the longest or shortest substring or subarray</td></tr>
<tr><td>Stack: the next greater item, matching brackets</td></tr>
<tr><td>DP with one loop: the number of ways, the best total</td></tr>
<tr><td>amount ≤ 10⁴</td><td>O(n × amount)</td><td>DP over every amount: Coin Change, subset that adds up to a target</td></tr>
<tr><td>Sorted array</td><td>any n</td><td>O(log n)</td><td>Binary search: find a target, or where it goes</td></tr>
<tr><td>Answer is a number to search for</td><td>answer up to 10⁹</td><td>O(n log m)</td><td>Binary search on the answer: the smallest X that works (Koko)</td></tr>
<tr><td>Intervals</td><td>n ≤ 10⁵</td><td>O(n log n)</td><td>Sort by start, then merge</td></tr>
<tr><td>Linked list</td><td>n ≤ 10⁴</td><td>O(n)</td><td>Dummy node; slow and fast pointers; reverse in place</td></tr>
<tr><td rowspan="2">Binary tree</td><td rowspan="2">n ≤ 10⁴ nodes</td><td rowspan="2">O(n)</td><td>DFS recursion: depth, diameter, validate BST</td></tr>
<tr><td>BFS with a queue: level by level</td></tr>
<tr><td rowspan="3">Grid</td><td rowspan="3">rows, cols ≤ 300</td><td rowspan="3">O(rows × cols)</td><td>DFS: count regions (Number of Islands, Flood Fill)</td></tr>
<tr><td>BFS: something spreading, the fewest steps (Rotting Oranges)</td></tr>
<tr><td>DP on a grid: count paths (Unique Paths)</td></tr>
<tr><td rowspan="4">Graph</td><td rowspan="4">V, E ≤ 10⁵</td><td rowspan="3">O(V + E)</td><td>DFS or BFS on an adjacency list: is there a path, connected parts</td></tr>
<tr><td>BFS: the fewest steps</td></tr>
<tr><td>Topological sort: prerequisites, an order to do things in</td></tr>
<tr><td>O(E log V)</td><td>Dijkstra with a heap: the cheapest path when edges have costs</td></tr>
<tr><td rowspan="2">Design a data structure</td><td rowspan="2">calls ≤ 10⁵</td><td>O(1) per call</td><td>Hash map + linked list (LRU Cache); stack of (value, min) (Min Stack)</td></tr>
<tr><td>O(log k) per call</td><td>Heap of size k (Kth Largest Element in a Stream)</td></tr>
</table>

k is the k in the question, m is the largest value, V is the number of nodes and E the
number of edges. A row passes if it takes under about 10⁷ steps, which Python does in
about a second.

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

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
```

### Hash map or set
- **Clue:** "seen this before?", counting, grouping
- **How:** store what you've seen, so each lookup is O(1)
- **Done:** Contains Duplicate, Group Anagrams, Top K Frequent Elements

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Running total + hash map
- **Clue:** a contiguous subarray whose sum is k
- **How:** the sum from i to j is the total at j minus the total before i, so look up
  `total - k` in the map
- **Done:** Subarray Sum Equals K

```python
def subarray_sum(nums, k):
    count = total = 0
    seen = {0: 1}  # running total -> how many times we've had it
    for num in nums:
        total += num
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
```

### Sliding window
- **Clue:** the longest or shortest *contiguous* substring or subarray that follows
  a rule
- **How:** grow the right end. When the rule breaks, shrink from the left until it
  holds again.
- **Done:** Longest Substring Without Repeating Characters, Best Time to Buy and Sell
  Stock

```python
def longest_unique(s):
    window = set()
    left = best = 0
    for right, ch in enumerate(s):
        while ch in window:  # rule broken: shrink from the left
            window.remove(s[left])
            left += 1
        window.add(ch)
        best = max(best, right - left + 1)
    return best
```

### Binary search
- **Clue:** sorted input, or "the smallest X that works" where checking one X is easy
- **How:** check the middle and throw away the half that can't hold the answer
- **Done:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko Eating
  Bananas

Find a target in a sorted list:

```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Find the smallest X that works, as in Koko:

```python
def smallest_that_works(low, high, works):
    while low < high:
        mid = (low + high) // 2  # round down
        if works(mid):
            high = mid  # mid might be the answer, so keep it
        else:
            low = mid + 1
    return low
```

Keep the pairs together: `high = mid - 1` goes with `while low <= high`, and
`high = mid` goes with `while low < high` and rounding down.

### Stack
- **Clue:** the next greater or warmer item; matching brackets
- **How:** keep the items still waiting for an answer, and pop each one when its
  answer arrives
- **Done:** Daily Temperatures, Valid Parentheses

```python
def daily_temps(temps):
    answer = [0] * len(temps)
    stack = []  # indices still waiting for a warmer day
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

### Heap
- **Clue:** the k largest, smallest or closest
- **How:** keep a heap of size k (`heapq` is a min-heap)
- **Done:** Kth Largest Element in an Array, K Closest Points to Origin

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # drop the smallest
    return heap[0]
```

### DFS or BFS
- **Clue:** regions in a grid, something spreading, the fewest steps
- **How:** visit a cell, mark it, then visit its neighbours. Use BFS (a queue) when
  you need the fewest steps.
- **Done:** Number of Islands, Rotting Oranges

DFS, which counts islands:

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # mark as visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
```

BFS, which finds the fewest steps. Replace `neighbours(node)` with the problem's own
moves:

```python
from collections import deque

def bfs_steps(start, goal):
    queue = deque([start])
    seen = {start}
    steps = 0
    while queue:
        for _ in range(len(queue)):  # everything at this distance
            node = queue.popleft()
            if node == goal:
                return steps
            for nxt in neighbours(node):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        steps += 1
    return -1
```

### Tree recursion
- **Clue:** any binary tree
- **How:** solve for the left and right subtrees, then combine them. For level by
  level, use the BFS template above.
- **Done:** Validate Binary Search Tree, Binary Tree Level Order Traversal

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### Sort, then merge
- **Clue:** overlapping intervals
- **How:** sort by start. If the next interval starts before the current one ends,
  merge them.
- **Done:** Merge Intervals

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Dynamic programming
- **Clue:** the number of ways; the fewest, most or best total; "can you make X?";
  each choice depends on earlier ones
- **How:** answer four questions before coding:
  1. What does `dp[i]` mean? Say it in words, like "the number of ways to reach
     step i".
  2. How is `dp[i]` built from smaller answers? Look at the last choice made.
  3. What are the base cases, like `dp[0]`?
  4. Where is the answer: `dp[n]`, or `max(dp)`?
- **Done:** Climbing Stairs, House Robber

| Pattern | Clue | `dp[i]` means | Built from |
|---|---|---|---|
| One line | steps, houses in a row | the answer for the first i items | `dp[i - 1]` and `dp[i - 2]` |
| Ends at i | longest increasing subsequence | the best that ends exactly at i | every `dp[j]` with j < i |
| Split a string | can s be split into words? | `s[:i]` can be split | `dp[j]` where `s[j:i]` is a word |
| Make an amount | coins, as many of each as you like | the fewest coins that make amount a | `dp[a - coin]` for each coin |
| Use each once | a subset that adds up to a target | some numbers add up to s | `dp[s - num]`, with s going down |
| Grid | paths through a grid | the answer at cell (r, c) | the cell above and the cell to the left |
| Two strings | common subsequence, edit distance | the answer for `a[:i]` and `b[:j]` | `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]` |

One line, as a table (Climbing Stairs):

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = ways to reach step i
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # last move was 1 step, or 2 steps
    return dp[n]
```

The same, top-down: write the plain recursion, then add `@cache` so each `i` is
worked out only once. Python stops recursion about 1,000 calls deep, so for a bigger n
use the table.

```python
from functools import cache

def climb_stairs(n):
    @cache
    def ways(i):  # ways to reach step i
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)
```

One line, with two variables instead of a list (House Robber):

```python
def rob(nums):
    prev2 = prev1 = 0  # best up to i - 2, best up to i - 1
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # skip it, or take it
    return prev1
```

Ends at i (Longest Increasing Subsequence):

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = longest increasing subsequence that ends at i
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i] can go after nums[j]
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Split a string (Word Break):

```python
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [True] + [False] * len(s)  # dp[i] = s[:i] can be split into words
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:  # s[:j] splits, and s[j:i] is a word
                dp[i] = True
                break
    return dp[-1]
```

Make an amount (Coin Change):

```python
from math import inf

def coin_change(coins, amount):
    dp = [0] + [inf] * amount  # dp[a] = fewest coins that make a
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)  # the last coin was `coin`
    return dp[amount] if dp[amount] != inf else -1
```

Use each once (Partition Equal Subset Sum). Going down means `dp[s - num]` still
holds the answer from before this number, so it isn't used twice:

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target  # dp[s] = some numbers so far add up to s
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]  # without num, or with it
    return dp[target]
```

Grid (Unique Paths):

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = paths to (r, c); edges have 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # came from above, or from the left
    return dp[-1][-1]
```

Two strings (Longest Common Subsequence). Row 0 and column 0 stand for an empty
string, so they stay 0:

```python
def longest_common_subsequence(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]  # dp[i][j] = answer for a[:i], b[:j]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # last letters match: keep both
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop a letter from a, or from b
    return dp[-1][-1]
```

### Linked list tricks
- **Clue:** any linked list
- **How:** a dummy node saves special cases for the head. For slow and fast pointers,
  fast moves 2 steps and slow moves 1.
- **Done:** Linked List Cycle, Remove Nth Node From End of List

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
