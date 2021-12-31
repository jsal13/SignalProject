"""Sample Module."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, eq=True)
class Node:
    """Node object with ``x`` and ``y`` coordinate and an optional ``value``."""

    x: float
    y: float
    value: Optional[float] = None


@dataclass(frozen=True, eq=True)
class Edge:
    """
    Directed Edge object.

    ``source`` and ``dest`` are the source and destination
    :class:`~sensor.module1.Node` of the edge.
    """

    source: Node
    dest: Node
