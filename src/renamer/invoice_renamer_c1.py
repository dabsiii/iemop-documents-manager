import re
from pathlib import Path

from icecream import ic
from pypdf import PdfReader, PdfWriter

from src.renamer.invoice_renamer import InvoiceRenamer
from src.renamer.invoice_tracking_data.invoice_tracking_data_c2 import (
    InvoiceNumberNotFound,
    InvoiceTrackingDataC2,
)


class InvoiceRenamerC1(InvoiceRenamer):
    def __init__(self):
        pass

    def rename_booklet(
        self,
        scanned_booklet_path: Path,
        booklet_number_start: int,
        invoice_tracking_filename: Path,
        sheet_name: str,
        output_path: Path,
    ):

        output_path.mkdir(parents=True, exist_ok=True)
        reader = PdfReader(scanned_booklet_path)
        table = InvoiceTrackingDataC2(invoice_tracking_filename, sheet_name)

        for i, page in enumerate(reader.pages):

            writer = PdfWriter()
            writer.add_page(page)
            invoice_number = i + booklet_number_start
            ic(invoice_number)
            try:
                file_name = table.get_filename_from_invoice_number(invoice_number)
                output_filename = output_path / f"{file_name}.pdf"
                with output_filename.open("wb") as output_file:
                    writer.write(output_file)
            except InvoiceNumberNotFound:
                ic(f"invoice number {invoice_number} not listed")
