"""Local test harness for the solutions/ exercises.

Installed into the project venv by `uv sync`, so each solution file can just
`from interview_prep import run` with no path juggling.
"""
from .harness import (
    Node,
    TreeNode,
    build_graph,
    build_tree,
    find_node,
    graph_to_adj,
    run,
    run_design,
    tree_to_list,
)

__all__ = [
    "Node",
    "TreeNode",
    "build_graph",
    "build_tree",
    "find_node",
    "graph_to_adj",
    "run",
    "run_design",
    "tree_to_list",
]
