"""Local test harness for the solutions/ exercises.

Installed into the project venv by `uv sync`, so each solution file can just
`from interview_prep import run` with no path juggling.
"""
from .harness import (
    ListNode,
    Node,
    TreeNode,
    build_graph,
    build_linked_list,
    build_tree,
    find_node,
    graph_to_adj,
    linked_list_to_list,
    run,
    run_design,
    tree_to_list,
)

__all__ = [
    "ListNode",
    "Node",
    "TreeNode",
    "build_graph",
    "build_linked_list",
    "build_tree",
    "find_node",
    "graph_to_adj",
    "linked_list_to_list",
    "run",
    "run_design",
    "tree_to_list",
]
