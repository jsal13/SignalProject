"""Tests for ``sensor/generate_signals``."""

from sensor.generate_signals import Signal, clamp, generate_random_signal


def test_clamp() -> None:
    """Tests the clamp function."""
    assert clamp(110, 0, 100) == 100
    assert clamp(-100, 0, 100) == 0


def test_generate_random_signal() -> None:
    """Tests the random signal function."""
    assert isinstance(generate_random_signal(), Signal)
