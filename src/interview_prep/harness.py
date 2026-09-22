"""Local test harness for the example cases. Not part of any solution.

Each file under solutions/ calls run(...) from its __main__ block, so that
`python3 solutions/<topic>/<problem>.py` checks your code against LeetCode's
own worked examples. Nothing here is needed to solve anything.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Node:
    """Graph node, as used by Clone Graph."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_tree(vals):
    """LeetCode level-order list (with nulls) -> TreeNode."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """TreeNode -> level-order list, trailing nulls trimmed."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left); q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root, val):
    """Locate a node by value — LCA hands p and q over as plain values."""
    if not root:
        return None
    return (root if root.val == val
            else find_node(root.left, val) or find_node(root.right, val))


def build_graph(adj):
    """Adjacency list (1-indexed, as LeetCode prints it) -> Node."""
    if not adj or adj == [[]] and len(adj) == 1 and not adj[0]:
        return Node(1) if adj == [[]] else None
    nodes = {i: Node(i) for i in range(1, len(adj) + 1)}
    for i, nbrs in enumerate(adj, 1):
        nodes[i].neighbors = [nodes[j] for j in nbrs]
    return nodes.get(1)


def graph_to_adj(node):
    """Node -> adjacency list, in LeetCode's printed form."""
    if not node:
        return []
    seen, q = {node.val: node}, deque([node])
    while q:
        cur = q.popleft()
        for n in cur.neighbors:
            if n.val not in seen:
                seen[n.val] = n; q.append(n)
    return [[n.val for n in seen[k].neighbors] for k in sorted(seen)]


def _norm(x, any_order):
    if not any_order or not isinstance(x, list):
        return x
    inner = [sorted(i) if isinstance(i, list) else i for i in x]
    return sorted(inner, key=repr)


def run(fn, cases, *, any_order=False):
    """Run `fn` over (args, expected) pairs and report."""
    passed = 0
    for i, (args, want) in enumerate(cases, 1):
        try:
            got = fn(*args)
        except NotImplementedError:
            print("not implemented yet — solve it first, then paste your code in")
            return
        except Exception as e:
            print(f"  case {i}  ERROR  {type(e).__name__}: {e}")
            continue
        ok = _norm(got, any_order) == _norm(want, any_order)
        passed += ok
        print(f"  case {i}  {'pass' if ok else 'FAIL'}"
              + ("" if ok else f"   got {got!r}\n          want {want!r}"))
    print(f"\n{passed}/{len(cases)} passed")


def run_design(cls, cases):
    """Design problems: a list of operations against one object."""
    passed = 0
    for i, ((ops, args), want) in enumerate(cases, 1):
        got = []
        try:
            obj = None
            for op, a in zip(ops, args):
                if op == ops[0] and obj is None:
                    obj = cls(*a); got.append(None)
                else:
                    got.append(getattr(obj, op)(*a))
        except NotImplementedError:
            print("not implemented yet — solve it first, then paste your code in")
            return
        except Exception as e:
            print(f"  case {i}  ERROR  {type(e).__name__}: {e}")
            continue
        ok = got == want
        passed += ok
        print(f"  case {i}  {'pass' if ok else 'FAIL'}"
              + ("" if ok else f"\n    got  {got}\n    want {want}"))
    print(f"\n{passed}/{len(cases)} passed")
