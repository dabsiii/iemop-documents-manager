import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from src.gui.booklet_gui.booklet_gui import BookletGui

from src.renamer.booklet.booklet_c1 import Booklet, BookletC1

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1
from src.renamer.invoice_tracking_data.invoice_tracking_data_c3 import (
    InvoiceTrackingDataC3,
    InvoiceTrackingData,
)
from pathlib import Path


from icecream import ic


class BookletRenamer:
    def __init__(self, booklet: Booklet, tracker_data: InvoiceTrackingData):
        self._booklet = booklet
        self._tracker_data = tracker_data

    def get_widget(self):
        self._gui = BookletGui()
        self._gui.commanded_rename.subscribe(self.individual_rename)

        start = self._booklet.get_starting_number()
        final = self._booklet.get_final_number()
        title = f"Booklet {start}-{final}  (.pdf)"
        self._gui.set_title(title)

        return self._gui.widget

    def individual_rename(self):
        directory = qtw.QFileDialog.getExistingDirectory(None, "Select Output Location")
        self.rename_booklet(directory)

    def rename_booklet(self, output_dir):
        renamer = InvoiceRenamerC1()
        try:
            start = self._booklet.get_starting_number()
            output_path = Path(output_dir).resolve()
            renamer.rename_booklet(
                scanned_booklet_path=self._gui.get_booklet_path(),
                booklet_number_start=start,
                tracking_data=self._tracker_data,
                output_path=output_path,
            )
            self._gui.show_info(
                "Done",
                f"""
Invoices Renamed Succesfuly. 
Transaction Reference: {self._tracker_data.get_transaction_number()} 
Booklets {start}-{start+49} 

Output Location: {output_path}""",
            )
        except Exception as e:
            ic(e)
            self._gui.show_error(
                "Error", "Unexpected Error Occured, please check your inputs."
            )

    def ready(self):
        return self._gui.ready
