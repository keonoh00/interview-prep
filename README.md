# interview-prep

43 problems for a live DS&A screen on **Friday 2 October 2026**. Each file under
`solutions/` holds the LeetCode description, the stub, and the worked examples as
runnable tests.

## Running

```bash
uv sync                                           # once
uv run solutions/hash-maps/contains_duplicate.py  # one problem
```

Replace `raise NotImplementedError` with your code and it checks against LeetCode's
own examples.

Once LeetCode accepts your solution, ask Claude to check it. If it's reasonable,
Claude says so briefly, with its time and space complexity, and you move on. If it
misses what the question is teaching, Claude stops you and gives a hint.

## The header

Each file records its own result on the fourth line:

```python
# Contains Duplicate — Easy (#217)
# https://leetcode.com/problems/contains-duplicate/
# Day 1 · Tue 22 Sep
# not yet attempted       ->   2026-09-22 | 18 min | unaided: yes | CLEAR
```

`STAR` instead of `CLEAR` if it took more than 25 minutes unaided, or the approach
was not optimal.

```bash
grep -rl 'not yet attempted' solutions/   # what is left
grep -rl '| STAR' solutions/              # what to redo
```

## Time and space complexity

Complexity describes how the cost of your code grows as the input grows. **Time** is
how many steps it takes. **Space** is how much extra memory it creates. Both are
written in big-O, where n is the size of the input, such as `len(nums)`.

| Big-O | What it means | Where you'll see it |
|---|---|---|
| O(1) | Same work for any input size | `x in a_set`, `d[key]`, `nums[i]` |
| O(log n) | The input is halved at each step | Binary Search |
| O(n) | Double the input, double the work | one `for` loop, `set(nums)` |
| O(n log n) | A bit more than O(n) | `sorted(nums)`, `nums.sort()` |
| O(n²) | Double the input, four times the work | a loop inside a loop |

To work out the time of your code:

1. Say what n is, for example `n = len(nums)`.
2. Look at the loops. One loop over the input is O(n). A loop inside a loop is
   O(n²). Halving the range at each step is O(log n).
3. Count the built-ins too. `sorted()` is O(n log n), and `x in some_list` is O(n),
   but `x in some_set` and `x in some_dict` are O(1).
4. Keep only the biggest part and drop constant factors: O(n + n log n) is
   O(n log n), and O(2n) is O(n).

For space, count only the memory your code creates (sets, dicts, new lists), not the
input. A few plain variables are O(1).

**Is it fast enough?** Look at the constraints under the problem. If n can be 10^5,
O(n²) means about 10^10 steps and will time out, so aim for O(n) or O(n log n). If n
is at most about 1,000, O(n²) is only about 10^6 steps and is fine.
