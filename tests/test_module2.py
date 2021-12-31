"""Tests Module1."""

from sensor.module1 import Node, Edge
from sensor.module2 import Graph


def test_node():
    """Tests the Node object."""
    test_nodes = [Node(1, 2), Node(2, 3), Node(3, 4), Node(4, 5)]
    test_edges = [Edge(test_nodes[0], test_nodes[1])]
    graph = Graph(nodes=test_nodes, edges=test_edges)

    assert graph.count_nodes() == 4
    assert graph.has_an_edge(test_edges[0].source, test_edges[0].dest)
