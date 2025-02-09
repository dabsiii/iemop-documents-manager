from src.gui.home import Home
from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceTrackingDataC3,
)

from src.booklet_renamer import BookletRenamer

from icecream import ic

from typing import List


class App:
    def __init__(self):
        self._home = Home()
        self._renamers: List[BookletRenamer] = []

    def _setup_events(self):
        self._home.selected_tracking_data.subscribe(self._try_initialize_tracker)
        self._home.clicked_rename_button.subscribe(lambda e: self._rename())

    def start(self):
        self._setup_events()
        self._home.show()

    def _initialize_tracker(self):
        tracker_data_path = self._home.get_tracker_data_path()
        tracker = InvoiceTrackingDataC3(tracker_data_path)

        booklets = sorted(tracker.get_required_booklets())
        self._renamers = []
        for booklet in booklets:
            renamer = BookletRenamer(booklet, tracker)
            self._renamers.append(renamer)

        renamer_widgets = [renamer.get_widget() for renamer in self._renamers]
        self._home.display_on_scroll(renamer_widgets)

    def _try_initialize_tracker(self):
        tracker_data_path = self._home.get_tracker_data_path()
        if tracker_data_path is None:
            self._home.clear_scroll()

        else:
            try:
                self._initialize_tracker()
            except Exception as e:
                ic(e)
                self._home.display_invalid_tracker_data_file()
