import re
from pathlib import Path

from icecream import ic
from pypdf import PdfReader, PdfWriter

from src.renamer.filename_table.filename_table_c1 import FilenameTableC1
from src.renamer.invoice_renamer import InvoiceRenamer


class InvoiceRenamerC1(InvoiceRenamer):
    def rename_booklet(
        self,
        scanned_booklet_path: Path,
        booklet_number_start: Path,
        file_name_table: Path,
        output_path: Path,
    ):

        output_path.mkdir(parents=True, exist_ok=True)
        reader = PdfReader(scanned_booklet_path)
        table = FilenameTableC1(file_name_table)

        for i, page in enumerate(reader.pages, start=1):
            ic(i)
            writer = PdfWriter()
            writer.add_page(page)
            invoice_number = i + booklet_number_start

            file_name = table.get_filename_from_invoice_number(invoice_number)
            output_filename = output_path / f"{file_name}.pdf"

            with output_filename.open("wb") as output_file:
                writer.write(output_file)
