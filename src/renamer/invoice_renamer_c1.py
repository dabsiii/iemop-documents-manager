import re
from pathlib import Path

from icecream import ic
from pypdf import PdfReader, PdfWriter

from src.renamer.invoice_renamer import InvoiceRenamer
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceNumberNotFound,
    InvoiceTrackingDataC3,
    InvoiceTrackingData,
)


class InvoiceRenamerC1(InvoiceRenamer):
    def __init__(self):
        pass

    def get_number_of_pages(self, pdf_path: Path) -> int:
        reader = PdfReader(pdf_path)
        return len(reader.pages)

    def rename_booklet(
        self,
        scanned_booklet_path: Path,
        booklet_number_start: int,
        tracking_data: InvoiceTrackingData,
        # sheet_name: str,
        output_path: Path,
    ):
        container = (
            output_path
            / f"Invoices {tracking_data.get_transaction_number()} Booklet {booklet_number_start}-{booklet_number_start+49}"
        )
        output_path = container
        output_path.mkdir(parents=True, exist_ok=True)
        reader = PdfReader(scanned_booklet_path)
        table = tracking_data

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
