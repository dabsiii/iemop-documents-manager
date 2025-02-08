from src.gui.home import Home
from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceTrackingDataC3,
)


from icecream import ic


class App:
    def __init__(self):
        self._home = Home()

    def _setup_events(self):
        self._home.selected_tracking_data.subscribe(self._initialize_tracker)

    def start(self):
        self._setup_events()
        self._home.show()

    def _initialize_tracker(self):
        tracker_data_path = self._home.get_tracker_data_path()
        tracker = InvoiceTrackingDataC3(tracker_data_path)
        ic(tracker.get_required_booklets())
