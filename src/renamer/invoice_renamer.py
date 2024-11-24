from abc import ABC, abstractmethod
from pathlib import Path


class InvoiceRenamer(ABC):
    @abstractmethod
    def rename_booklet(
        self,
        booklet_pdf_path: Path,
        booklet_number_start: int,
        file_name_table: Path,
        output_path: Path,
    ): ...
