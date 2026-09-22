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
