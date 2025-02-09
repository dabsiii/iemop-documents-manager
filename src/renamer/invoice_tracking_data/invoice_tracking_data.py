from abc import ABC, abstractmethod


class InvoiceTrackingData(ABC):
    @abstractmethod
    def get_filename_from_invoice_number(self, invoice_number: int) -> str: ...

    @abstractmethod
    def get_transaction_number(self) -> str: ...
