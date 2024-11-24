from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def split_pdf(pdf_path: Path, output_dir: Path):

    if not pdf_path.is_file():
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(pdf_path)

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = output_dir / f"Page_{i}.pdf"

        with output_filename.open("wb") as output_file:
            writer.write(output_file)


pdf_path = Path("src\\scanned_invoice\\sample.pdf").resolve()
output_dir = Path("src\\scanned_invoice\\output").resolve()
split_pdf(pdf_path, output_dir)
