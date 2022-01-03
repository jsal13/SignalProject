"""Streamlit app for displaying data."""

from typing import Any

import altair as alt
import numpy as np
import pandas as pd
import requests as req
import streamlit as st
from st_aggrid import AgGrid


def get_sensor_data() -> pd.DataFrame:
    """Get sensor data from the API."""
    raw_data = req.get("http://localhost:8000/sensors/").json()["data"]
    _df = pd.DataFrame(raw_data)[["datetime", "sensor", "value"]]
    _df["datetime"] = pd.to_datetime(_df["datetime"])
    return _df


# TODO: Figure out typing on this.
def normalize_vector(arr: Any) -> Any:
    """Normalize vector ``arr``."""
    norm = np.linalg.norm(arr)
    if norm == 0:
        return arr
    return arr / norm


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize the signal data."""
    for sensor in df["sensor"].unique():
        sensor_mask = df["sensor"] == sensor
        df.loc[sensor_mask, "value"] = normalize_vector(df["value"][sensor_mask])

    return df


df_0 = get_sensor_data()
df_0 = normalize_data(df_0)

chart = alt.Chart(df_0).mark_line().encode(x="datetime:T", y="value", color="sensor:N")

# -- Begin Streamlit --
st.header("Sensor Data")

with st.empty():
    st.altair_chart(chart.interactive(), use_container_width=True)

with st.expander("Data Table"):
    AgGrid(df_0)
