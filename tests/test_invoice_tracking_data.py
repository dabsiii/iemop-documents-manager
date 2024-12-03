from pathlib import Path

from icecream import ic

from src.renamer.invoice_tracking_data.invoice_tracking_data_c2 import (
    InvoiceTrackingDataC2,
)


def test_1():
    rel_path = Path("tests\\files\\INVOICE WRITING.xlsx")
    abs_path = rel_path.resolve()
    table = InvoiceTrackingDataC2(abs_path, "202409")
    #filename = table.get_filename_from_invoice_number(9351)
    #ic(filename)


def test_2():
    rel_path = Path("tests\\files\\INVOICE WRITING.xlsx")
    abs_path = rel_path.resolve()
    table = InvoiceTrackingDataC2(abs_path, "202409")
    ic(table._excel_data)
    filename = table.get_filename_from_invoice_number(8150)
    ic(filename)
