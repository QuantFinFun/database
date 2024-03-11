"""
    Common functions/scripts to be used among the scripts
    present in this module
"""
__author__ = "Mohd Sadiq"
__version__ = "v0.1"


import os
from typing import Any, List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_entry_to_database(objects: List[Any]):
    """
    This Function takes in a list of objects
    and adds them to their respective tables in
    the database
    """
    engine = create_engine(str(os.getenv("DB_URL")))

    with Session(engine) as session:
        session.add_all(objects)
        session.commit()


def price_entry_json(index: str, asset: str, row: Any):
    """
    This function builds a dictionary and returns it
    to the respective scripts that need to populate according
    to the price data
    """
    entry_dict = {
        "date": index,
        "asset": asset,
        "open": float(row["Open"]),
        "high": float(row["High"]),
        "low": float(row["Low"]),
        "close": float(row["Close"]),
        "volume": int(row["Volume"]),
        "dividends": float(row["Dividends"]),
        "stock_split": float(row["Stock Splits"]),
    }

    return entry_dict
