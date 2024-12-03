from pathlib import Path

import pandas
from pandas import DataFrame, Series

from src.renamer.invoice_tracking_data.invoice_tracking_data import InvoiceTrackingData


class InvoiceTrackingDataC1(InvoiceTrackingData):
    INVOICE_NUMBER_COLUMN = "INVOICE NUMBER"
    FILENAME_COLUMN = "REFERENCE"

    def __init__(self, table_filepath: Path):
        excel_data = pandas.read_excel(table_filepath, sheet_name=None)
        self._all_data = pandas.concat(excel_data.values(), ignore_index=True)

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
        filtered_df = self._all_data[
            self._all_data[self.INVOICE_NUMBER_COLUMN] == target_value
        ]
        return filtered_df


class InvoiceNumberNotFound(Exception):
    """When the invoice number is not on the table"""

    def __init__(self, message: str):
        super().__init__(message)


class MultipleInvoiceNumberEntry(Exception):
    """When more than one invoice number is entered on the record"""

    def __init__(self, message: str):
        super().__init__(message)
