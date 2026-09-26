# Min Stack — Medium (#155)
# https://leetcode.com/problems/min-stack/
# Day 3 · Thu 24 Sep
# not yet attempted

r"""
Build a stack that can also tell you its smallest element, with every operation
taking constant time.

The MinStack class needs:

  - MinStack() sets up an empty stack.
  - push(value) puts value on top of the stack.
  - pop() takes the top element off.
  - top() returns the top element.
  - getMin() returns the smallest element currently in the stack.

Each of these must run in O(1) time.

Example 1:
    Input
    ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    [[], [-2], [0], [-3], [], [], [], []]
    Output
    [null, null, null, null, -3, null, 0, -2]
    Explanation
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.getMin()  # -3
    s.pop()
    s.top()     # 0
    s.getMin()  # -2

Constraints:
  - -2^31 <= value <= 2^31 - 1
  - pop, top and getMin are only ever called when the stack isn't empty.
  - At most 3 * 10^4 calls are made to push, pop, top and getMin in total.

Tags: stack, design"""

class MinStack:

    def __init__(self):
        raise NotImplementedError


    def push(self, value: int) -> None:
        raise NotImplementedError


    def pop(self) -> None:
        raise NotImplementedError


    def top(self) -> int:
        raise NotImplementedError


    def getMin(self) -> int:
        raise NotImplementedError



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

CASES = [
    (
        (['MinStack', 'push', 'push', 'push', 'getMin', 'pop', 'top', 'getMin'],
         [[], [-2], [0], [-3], [], [], [], []]),
        [None, None, None, None, -3, None, 0, -2],
    ),
]

if __name__ == "__main__":
    from interview_prep import run_design

    run_design(MinStack, CASES)
