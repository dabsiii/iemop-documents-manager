from abc import ABC, abstractmethod


class FilenameTable(ABC):
    @abstractmethod
    def get_filename_from_invoice_number(self, invoice_number: int) -> str: ...
