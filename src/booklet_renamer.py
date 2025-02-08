from src.gui.booklet_gui.booklet_gui import BookletGui

from src.renamer.booklet.booklet_c1 import Booklet, BookletC1

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceTrackingDataC3,
    InvoiceTrackingData,
)


class BookletRenamer:
    def __init__(self, booklet: Booklet, tracker_data: InvoiceTrackingData):
        self._booklet = booklet
        self._tracker_data = tracker_data

    def get_widget(self):
        gui = BookletGui()
        start = self._booklet.get_starting_number()
        final = self._booklet.get_final_number()
        title = f"Booklet {start}-{final}  (.pdf)"
        gui.set_title(title)

        return gui.widget
