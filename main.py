from pathlib import Path

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1

renamer = InvoiceRenamerC1()


BOOKLET_PATH = (
    "tests\\files\\booklets\\Scanned Booklets\\BOOKLET 6801-6850 (SCANNED).pdf"
)
BOOKLET_NUMBER_START = 6801
FILE_NAME_TABLE = Path("tests\\files\\Invoice_Tracking.xlsx").resolve()

SHEETNAME = "202409"
OUTPUT_PATH = Path(
    f"output\\period {SHEETNAME} bklt {BOOKLET_NUMBER_START}-{BOOKLET_NUMBER_START+49}"
).resolve()
renamer.rename_booklet(
    scanned_booklet_path=BOOKLET_PATH,
    booklet_number_start=BOOKLET_NUMBER_START,
    invoice_tracking_filename=FILE_NAME_TABLE,
    sheet_name=SHEETNAME,
    output_path=OUTPUT_PATH,
)
