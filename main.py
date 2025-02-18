from pathlib import Path

from icecream import ic

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceTrackingDataC3,
)

BOOKLET_NUMBER_START = 6751
BOOKLET_PATH = f"tests\\files\\booklets\\Scanned Booklets\\BOOKLET {BOOKLET_NUMBER_START}-{BOOKLET_NUMBER_START+49} (SCANNED).pdf"
FILE_NAME_TABLE = Path("tests\\files\\Invoice_Tracking.xlsx").resolve()
FILE_NAME_TABLE = Path("tests\\Invoice_Tracking - 202412.csv").resolve()

SHEETNAME = "202408"
OUTPUT_PATH = Path(
    f"output\\period {SHEETNAME} bklt {BOOKLET_NUMBER_START}-{BOOKLET_NUMBER_START+49}"
).resolve()


tracker = InvoiceTrackingDataC3(FILE_NAME_TABLE)
required = tracker.get_required_booklets()
ic(sorted(required))


# renamer = InvoiceRenamerC1()
# renamer.rename_booklet(
#     scanned_booklet_path=BOOKLET_PATH,
#     booklet_number_start=BOOKLET_NUMBER_START,
#     invoice_tracking_filename=FILE_NAME_TABLE,
#     sheet_name=SHEETNAME,
#     output_path=OUTPUT_PATH,
# )
