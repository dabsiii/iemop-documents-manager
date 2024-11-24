from pathlib import Path

from icecream import ic

from src.renamer.filename_table.filename_table_c1 import FilenameTableC1


def test_1():
    rel_path = Path("tests\\INVOICE WRITING.xlsx")
    abs_path = rel_path.resolve()
    table = FilenameTableC1(abs_path)
    filename = table.get_filename_from_invoice_number(9351)
    ic(filename)
