"""API to send generated signals to."""
import datetime
import os
import time
from typing import Any

import pandas as pd
import psycopg2  # type: ignore
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sensor.generate_signals import Signal

docker_flag = os.environ.get("IS_DOCKERIZED")
HOST = "db" if docker_flag is not None else "localhost"


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        try:
            self.conn = psycopg2.connect(
                f"dbname='{self.dbname}' user='{self.user}' "
                f"host='{self.host}' password='{self.password}'"
            )
        except psycopg2.OperationalError as error:
            raise error

    def _check_connection(self, max_retries: int = 3) -> bool:
        """
        Check the connection to the db.

        Parameters
        ----------
        max_retries : int, optional
            Number of retries to connect to the db, by default 3

        Returns
        -------
        bool
            True if a connection to the db exists
        """
        tries = 0
        connected = self.is_connected()
        while not connected and tries < max_retries:
            print("Not connected to db.  Attempting to connect...")
            tries += 1
            try:
                self.connect()
                connected = True
            except psycopg2.OperationalError:
                pass
            time.sleep(1)
        return connected

    def is_connected(self) -> bool:
        """Check connection to the db."""
        return self.conn is not None

    def query(self, q: str) -> pd.DataFrame:
        """
        Query the DB with ``q``.

        Parameters
        ----------
        q : str
            The PostgreSQL query

        Returns
        -------
        pd.DataFrame
            Returned rows
        """
        response_df = pd.read_sql(sql=q, con=self.conn)
        return response_df


class SensorDB:
    """Methods related to the Sensor Table."""

    def __init__(self, dbconn: DBConnection):
        """
        Methods related to the Sensor Table.

        Parameters
        ----------
        dbconn : DBConnection
            Database Connection object.
        """
        self.dbconn = dbconn

        # Connect to the db.
        self.dbconn.connect()

    def insert_signal(self, signal: Signal) -> None:
        """Insert `signal` data into DB."""
        if self.dbconn.is_connected():
            query = "insert into signals (datetime, sensor, value) VALUES (%s, %s, %s)"
            with self.dbconn.conn.cursor() as cur:  # type: ignore
                cur.execute(query, (datetime.datetime.now(), 1, signal.signal_1))
                cur.execute(query, (datetime.datetime.now(), 2, signal.signal_2))
                cur.execute(query, (datetime.datetime.now(), 3, signal.signal_3))
            self.dbconn.conn.commit()  # type: ignore


# -- MAIN INIT --

dbc = DBConnection(host=HOST)
sensorDB = SensorDB(dbc)

# -- ENDPOINTS --


@app.get("/")
async def read_root() -> dict[str, str]:
    """Test root of API."""
    return {"Hello": "World"}


@app.post("/signals/")
async def add_signal(signal: Signal) -> None:
    """Add signal to PG Database."""
    sensorDB.insert_signal(signal)


@app.get("/sensors/1")
async def query_sensor() -> dict[Any, Any]:
    """Get signal `1` data from the db."""
    if dbc.is_connected():
        q = "select * from signals where sensor=1"
        results = dbc.query(q)
        return {"data": results.to_dict("records")}

    return {"data": {}}
