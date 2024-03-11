"""
    This script is responsible for populating the
    us_treasry_database with the us treasury data
"""
__author__ = "Mohd Sadiq"
__version__ = "v0.1"
__module__ = "populate_treasury"

from typing import List

from scripts import add_entry_to_database, price_entry_json
from scripts.stock_downloader import StockDownloader
from tables.treasury_table import USTreasuryDatabase
from utils import build_logger

error_logger, console_logger = build_logger(__module__)


def fill_database(tickers: List[str]) -> None:
    """
    This script helps in populating the us treasury
    table with the relevant information
    """
    downloader = StockDownloader()

    for ticker in tickers:
        treasury_history = downloader.download_stocks(ticker)
        asset = ticker
        try:
            treasury_objects = []
            for index, row in treasury_history.iterrows():
                entry_dict = price_entry_json(str(index), asset, row)
                treasury_entry = USTreasuryDatabase(**entry_dict)
                treasury_objects.append(treasury_entry)
            add_entry_to_database(treasury_objects)
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error("%s, %s", error, ticker)

        console_logger.info("Finished Populating %s", asset)


if __name__ == "__main__":
    fill_database(["^IRX", "^FVX", "^TNX", "^TYX"])
