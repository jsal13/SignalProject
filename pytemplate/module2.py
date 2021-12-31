"""Create Graph Object from the Node and Edge objects in `module1`."""

from sensor.module1 import Edge, Node


class Graph:
    """
    Graph consisting of nodes and edges.

    Attributes
    ----------
    nodes : list[:class:`~sensor.module1.Node`]
        Nodes in the graph
    edges : list[:class:`~sensor.module1.Edge`]
        Directed edges in the graph
    """

    def __init__(self, nodes: list[Node], edges: list[Edge]):
        """
        Graph consisting of nodes and edges.

        Parameters
        ----------
        nodes : list[:class:`~sensor.module1.Node`]
            Nodes in the graph
        edges : list[:class:`~sensor.module1.Edge`]
            Directed edges in the graph
        """
        self.nodes = nodes
        self.edges = edges

    def count_nodes(self):
        """Compute the number of ``nodes``."""
        return len(self.nodes)

    def has_an_edge(self, source: Node, dest: Node) -> bool:
        """
        Check to see if there is an edge between ``source`` and ``dest``.

        Parameters
        ----------
        source : :class:`~sensor.module1.Node`
            Source node to check
        dest : :class:`~sensor.module1.Node`
            Destination node to check


        Returns
        -------
        bool
        """
        for edge in self.edges:
            if edge.source == source and edge.dest == dest:
                return True
        return False
