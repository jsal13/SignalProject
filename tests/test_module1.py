"""Tests Module1."""

from sensor.module1 import Node


def test_node():
    """Tests the Node object."""
    tests = [(Node(1, 2), (1, 2, None)), (Node(1, 2, 3), (1, 2, 3))]

    for test in tests:
        vals = (test[0].x, test[0].y, test[0].value)
        assert vals == test[1], f"Expected {test[1]}, got {vals}."
