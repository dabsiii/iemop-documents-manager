from pathlib import Path
from typing import List, Set

import pandas
from pandas import DataFrame, Series

from src.renamer.invoice_tracking_data.invoice_tracking_data import InvoiceTrackingData
from src.renamer.booklet.booklet_c1 import BookletC1, Booklet


class InvoiceTrackingDataC3(InvoiceTrackingData):
    INVOICE_NUMBER_COLUMN = "INVOICE NUMBER"
    FILENAME_COLUMN = "REFERENCE"

    def __init__(self, table_filepath: Path):
        self._data = pandas.read_csv(table_filepath)

    def get_filename_from_invoice_number(self, invoice_number: int) -> str:
        record = self._get_record(invoice_number)
        if len(record) == 1:
            return record[self.FILENAME_COLUMN].iloc[0]
        elif record.empty:
            message = f"Invoice number {invoice_number} not found in the table"
            raise InvoiceNumberNotFound(message)
        elif len(record) > 1:
            message = "more than one invoice number is entered on the record"
            raise MultipleInvoiceNumberEntry(message)
        else:
            raise ValueError()

    def _get_record(self, target_value) -> DataFrame:
        filtered_df = self._data[self._data[self.INVOICE_NUMBER_COLUMN] == target_value]
        return filtered_df

    def get_required_booklets(self) -> Set[Booklet]:
        invoice_numbers = self._data[self.INVOICE_NUMBER_COLUMN].tolist()
        required_booklets = set()
        for number in invoice_numbers:
            if is_integer(number):
                booklet = BookletC1(int(number))
                required_booklets.add(booklet)

        return required_booklets

    def get_transaction_number(self) -> str:
        sample_file_name = self._data.iloc[0, 0]
        transaction_number = sample_file_name.split("_")[3]
        return transaction_number


class InvoiceNumberNotFound(Exception):
    """When the invoice number is not on the table"""

    def __init__(self, message: str):
        super().__init__(message)


class MultipleInvoiceNumberEntry(Exception):
    """When more than one invoice number is entered on the record"""

    def __init__(self, message: str):
        super().__init__(message)


# def get_booklets_from_numbers(invoice_numbers: List[int]) -> List[str]:
#     """From the invoice numbers, detect which booklet it belongs"""
#     starts = []
#     for invoice_number in invoice_numbers:
#         starts.append(get_booklet_number_start(invoice_number))

#     starts_list = list(set(starts))
#     return [f"booklet {start}-{start+49}" for start in starts_list]


# def get_booklet_number_start(invoice_number):
#     remainder = invoice_number % 50
#     start = invoice_number - remainder + 1
#     if start > invoice_number:
#         return start - 50
#     return start


def is_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
