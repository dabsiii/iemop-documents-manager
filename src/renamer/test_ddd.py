from pathlib import Path
from typing import List

from PyPDF2 import PdfReader, PdfWriter


def rename_scanned_booklet(
    scanned_booklet: Path,
    booklet_number_start: int,
    file_name_table: Path,
    output_dir: Path,
):

    if not scanned_booklet.is_file():
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(scanned_booklet)

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        invoice_number = i + booklet_number_start
        output_filename = output_dir / f"Page_{invoice_number}.pdf"

        with output_filename.open("wb") as output_file:
            writer.write(output_file)
