# Choosing a technique

Before writing code, take about two minutes and say three things out loud:

1. **The constraints:** which algorithms will pass?
2. **The brute force:** what does it keep repeating?
3. **The clue in the wording:** which technique does it point to?

---

## Step 1: What do the constraints allow?

Find your n in the top row, then read down the column: ✅ will pass, ❌ will time
out. If your n falls between two columns, use the bigger one. For a grid, n is
rows × cols; for a graph, it's nodes + edges.

| Algorithm | n ≤ 10 | n ≤ 20 | n ≤ 100 | n ≤ 3,000 | n ≤ 10⁴ | n ≤ 10⁵ or more |
|---|---|---|---|---|---|---|
| Try every order (backtracking over permutations) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Try every subset: take it or skip it (backtracking) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Three nested loops: every triplet | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Two nested loops: every pair, or a 2D DP table | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Sort first; sort, then merge | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Heap | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Binary search inside a loop, or on the answer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hash map or set; running total + hash map | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Two pointers; sliding window | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Stack | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DFS or BFS; tree recursion | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DP with one loop | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Linked list tricks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Binary search on a sorted array | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

For example, `1 <= nums.length <= 10^5` is the last column: two nested loops time
out, so use sorting, a hash map, two pointers, a sliding window, and so on. ✅ means
it finishes in about a second in Python, which does about 10⁷ simple steps a second.

Other clues in the constraints:

| The constraints say | Algorithm |
|---|---|
| the array is sorted | binary search, or two pointers from both ends |
| the answer can be as big as 10⁹ | binary search on the answer: only about 30 tries |
| values can be as big as 10⁹ | a hash map, not a list indexed by value |
| only lowercase letters, or values in a small range like 0 to 100 | a count array such as `[0] * 26` instead of sorting |
| values can be negative | a sliding window on sums breaks, so use running total + hash map |
| a k is given | a heap of size k |
| a grid up to 300 × 300 | DFS or BFS over every cell |
| up to 10⁵ nodes and edges | DFS or BFS |
| "must run in O(log n)" | binary search |
| "O(n) time" on unsorted input | no sorting, so a hash set or count array |
| "O(1) extra space" | two pointers, slow and fast pointers, or change the input in place |

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
- **Clue:** the number of ways, or the best total where each choice depends on earlier
  ones
- **How:** build the answer for i from the answers for i - 1 and i - 2
- **Done:** Climbing Stairs, House Robber

```python
def rob(nums):
    prev2 = prev1 = 0  # best up to i - 2, best up to i - 1
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # skip it, or take it
    return prev1
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
