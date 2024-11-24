from pathlib import Path

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1

renamer = InvoiceRenamerC1()

BOOKLET_PATH = Path("tests\\sample_booklet.pdf").resolve()
BOOKLET_NUMBER_START = 9351
FILE_NAME_TABLE = Path("tests\\INVOICE WRITING.xlsx").resolve()
OUTPUT_PATH = Path("tests\\output renamed").resolve()

renamer.rename_booklet(
    scanned_booklet_path=BOOKLET_PATH,
    booklet_number_start=BOOKLET_NUMBER_START,
    file_name_table=FILE_NAME_TABLE,
    output_path=OUTPUT_PATH,
)
