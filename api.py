"""API to send generated signals to."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Test root of API."""
    return {"Hello": "World"}


@app.post("/signal/{signal_1}/{signal_2}/{signal_3}")
def signal_post(signal_1: float, signal_2: float, signal_3: float) -> None:
    """Print out the signal."""
    print(f"Got {signal_1}/{signal_2}/{signal_3}!")
    # TODO: db.
