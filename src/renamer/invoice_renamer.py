from abc import ABC, abstractmethod
from pathlib import Path


class InvoiceRenamer(ABC):
    @abstractmethod
    def rename_booklet(
        self,
        scanned_booklet_path: Path,
        booklet_number_start: Path,
        invoice_tracking_filename: Path,
        sheet_name: str,
        output_path: Path,
    ): ...
