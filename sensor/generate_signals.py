"""Generate signals for the sensor."""

import time
from dataclasses import dataclass

import numpy as np
import requests as req


@dataclass
class Signal:
    """Data Class for a Signal."""

    signal_1: float
    signal_2: float
    signal_3: float

    def as_tuple(self) -> tuple[float, float, float]:
        """Return signals as tuple."""
        return (self.signal_1, self.signal_2, self.signal_3)


def clamp(val: float, minimum: float, maximum: float) -> float:
    """
    Clamp `val` between `minimum` and `maximum` inclusive.

    Parameters
    ----------
    val : float
        Value to clamp.
    minimum : float
        Minimum desired value.
    maximum : float
        Maximum desired value.
    Returns
    -------
    float
    """
    return max(minimum, min(val, maximum))


def generate_random_signal() -> Signal:
    """Generate a random Signal."""
    signal_1 = clamp(50 + 20 * np.random.randn(), 0, 100)
    signal_2 = (
        2 * signal_1
        + 10 * np.random.randn()
        + np.random.choice(
            a=np.array([0, -60, 60]), p=np.array([0.995, 0.0025, 0.0025])
        )
    )
    signal_3 = signal_1 ** 2 + signal_2 + 20 * np.random.randn()

    return Signal(
        signal_1=round(signal_1, 3),
        signal_2=round(signal_2, 3),
        signal_3=round(signal_3, 3),
    )


def generate(
    endpoint: str = "http://127.0.0.1:8000/signal/", secs_between_signals: float = 1
) -> None:
    """
    Generate random signals.

    POST random signals to `endpoint` with delay `secs_between_signals`.

    Parameters
    ----------
    endpoint : Optional[str], default http://127.0.0.1:8000/signal/
        Endpoint to POST to.
    secs_between_signals : Optional[float], default 1
        Seconds to wait between each POST.
    """
    while True:
        data = generate_random_signal().as_tuple()
        q_string = "/".join(map(str, data))
        print(f"POSTing {endpoint + q_string}...")
        req.post(endpoint + q_string)
        time.sleep(secs_between_signals)


if __name__ == "__main__":
    generate(secs_between_signals=3)
