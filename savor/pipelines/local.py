"""
Savor Data Pipeline :: Airtable -> Local

- Retrieves data from Airtable
- Loads it into local Postgres instance
"""

# %% Imports
from os import environ
from pathlib import Path
from typing import List, Dict

from airtable import Airtable
from dotenv import load_dotenv
import pandas as pd

# %%
class AirPipe:
    """Savor data pipeline: from Airtable to (local) Postgres."""

    def __init__(
        self,
        base_key: str,
        api_key: str,
        pg_conn: str,
        tables,
    ) -> None:
        """Constructor for Airtable pipeline.
        Connects to Airtable and Postgres upon instantiation.

        :param base_key (str) : Airtable base key.
        :param api_key (str) : Airtable API key.
        :param pg_conn (str) : Connection string for Postgres data warehouse.
        :param tables (List[str] or Dict[str, str]) : If Airtable and DWH table names are identical
            pass list of names. If not, pass dict mapping of table names: `{airtable : dwh}`.
        """
        # Set instance vars / attributes
        self.base_key = base_key
        self.api_key = api_key
        self.pg_conn = pg_conn

        # If list of table names is passed, set up as dict
        if isinstance(tables, list):
            self.tables = {t: t for t in tables}
        elif isinstance(tables, dict):
            self.tables = tables
        else:  # If neither, raise exception
            raise TypeError("Invalid tables list or mapping.")

        # Pipeline state variables
        self.cur_data = []
