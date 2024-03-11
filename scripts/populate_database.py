"""
    This script is responsible for populating the
    stock_price_dataset with the stock price information
"""
__author__ = "Mohd Sadiq"
__version__ = "v0.1"
__module__ = "populate_database"

from typing import List

import pandas as pd

from scripts import add_entry_to_database, price_entry_json
from scripts.stock_downloader import StockDownloader
from tables.stock_price import StockPriceDataset
from utils import build_logger

error_logger, console_logger = build_logger(__module__)


def get_snp_500() -> List[str]:
    """
    This script gets the S&P500 asset tickers
    """
    tickers = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    )[0]

    return list(tickers["Symbol"].iloc[:].values)


def fill_database(tickers: List[str]) -> None:
    """
    This script helps in populating the stock_price_dataset
    table with the relevant information
    """
    downloader = StockDownloader()

    for ticker in tickers:
        stock_price_history = downloader.download_stocks(ticker)
        asset = ticker
        try:
            stock_history_objects = []
            for index, row in stock_price_history.iterrows():
                entry_dict = price_entry_json(str(index), asset, row)
                stock_price_entry = StockPriceDataset(**entry_dict)
                stock_history_objects.append(stock_price_entry)
            add_entry_to_database(stock_history_objects)
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error("%s, %s", error, ticker)

        console_logger.info("Finished Populating %s", asset)


if __name__ == "__main__":
    fill_database(get_snp_500())
