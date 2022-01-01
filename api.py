"""API to send generated signals to."""
import datetime
import time

import psycopg2  # type: ignore
from fastapi import FastAPI

from sensor.generate_signals import Signal

app = FastAPI()


class DBConnection:
    """Handle connection data for the DB."""

    def __init__(
        self,
        dbname: str = "postgres",
        user: str = "postgres",
        host: str = "db",  # docker-compose alias.
        password: str = "x",
    ):
        """
        Handle connection data for the DB.

        Parameters
        ----------
        dbname : str, optional
            Name of the database, by default "postgres"
        user : str, optional
            User name, by default "postgres"
        host : str, optional
            Host name, by default "db"
        password : str, optional
            Password, by default "x"
        """
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.conn = None

    def connect(self) -> None:
        """Connect to the DB."""
        self.conn = psycopg2.connect(
            f"dbname='{self.dbname}' user='{self.user}' "
            f"host='{self.host}' password='{self.password}'"
        )

    def is_connected(self) -> bool:
        """Check connection to the db."""
        return self.conn is not None


dbc = DBConnection()


@app.get("/")
async def read_root() -> dict[str, str]:
    """Test root of API."""
    return {"Hello": "World"}


@app.post("/signals/")
async def add_signal(signal: Signal) -> None:
    """Add signal to PG Database."""
    if not dbc.is_connected():
        print("Not connected to db.  Attempting to connect...")
        dbc.connect()
        time.sleep(1)

    if dbc.is_connected():
        query = "insert into signals (datetime, sensor, value) VALUES (%s, %s, %s)"
        with dbc.conn.cursor() as cur:  # type: ignore
            print(query % (datetime.datetime.now(), 1, signal.signal_1))
            cur.execute(query, (datetime.datetime.now(), 1, signal.signal_1))
            cur.execute(query, (datetime.datetime.now(), 2, signal.signal_2))
            cur.execute(query, (datetime.datetime.now(), 3, signal.signal_3))
        dbc.conn.commit()  # type: ignore
