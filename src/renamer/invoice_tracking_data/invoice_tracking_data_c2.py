from pathlib import Path
from typing import List

import pandas
from pandas import DataFrame, Series

from src.renamer.invoice_tracking_data.invoice_tracking_data import InvoiceTrackingData


class InvoiceTrackingDataC2(InvoiceTrackingData):
    INVOICE_NUMBER_COLUMN = "INVOICE NUMBER"
    FILENAME_COLUMN = "REFERENCE"

    def __init__(self, table_filepath: Path, sheet_name: str):
        self._excel_data = pandas.read_excel(table_filepath, sheet_name=sheet_name)
        # sheets_dict = pandas.read_excel(excel_file, sheet_name=None)

        # Extract the DataFrames as a list
        # self._dataframes_list = list(excel_data.values())

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
        filtered_df = self._excel_data[
            self._excel_data[self.INVOICE_NUMBER_COLUMN] == target_value
        ]
        return filtered_df

    def get_required_booklets(self) -> List[str]:
        invoice_numbers = self._excel_data[self.INVOICE_NUMBER_COLUMN].tolist()
        invoice_numbers = [
            int(number) for number in invoice_numbers if is_integer(number)
        ]
        return get_booklets_from_numbers(invoice_numbers)


class InvoiceNumberNotFound(Exception):
    """When the invoice number is not on the table"""

    def __init__(self, message: str):
        super().__init__(message)


class MultipleInvoiceNumberEntry(Exception):
    """When more than one invoice number is entered on the record"""

    def __init__(self, message: str):
        super().__init__(message)


def get_booklets_from_numbers(invoice_numbers: List[int]) -> List[str]:
    """From the invoice numbers, detect which booklet it belongs"""
    starts = []
    for invoice_number in invoice_numbers:
        starts.append(get_booklet_number_start(invoice_number))

    starts_list = list(set(starts))
    return [f"booklet {start}-{start+49}" for start in starts_list]


def get_booklet_number_start(invoice_number):
    remainder = invoice_number % 50
    start = invoice_number - remainder + 1
    if start > invoice_number:
        return start - 50
    return start


def is_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
