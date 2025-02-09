import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


import sys
from src.gui.selector.selector_c1 import SelectorC1
from pathlib import Path

from icecream import ic


from src.events.event_ import Event_, Event
from datetime import datetime

from src.renamer.invoice_renamer_c1 import InvoiceRenamerC1


class BookletGui:
    def __init__(self):
        self._init_ui()
        self._setup_events()
        self.ready = False
        self.commanded_rename = Event_()

    # self.selected = Event_()

    def _init_ui(self):
        self._widget = qtw.QWidget()
        widget_layout = qtw.QVBoxLayout()
        self._widget.setLayout(widget_layout)

        self._frame = qtw.QFrame()

        self._frame.setObjectName("frame")

        self._frame.setStyleSheet(
            "#frame { border: 1px solid black; border-radius: 5px; background-color: orange;}"
        )
        frame_layout = qtw.QVBoxLayout()
        self._frame.setLayout(frame_layout)
        widget_layout.addWidget(self._frame)

        hlayout = qtw.QHBoxLayout()
        frame_layout.addLayout(hlayout)

        self._selector = SelectorC1()
        self._selector.set_file_types("pdf")
        hlayout.addWidget(self._selector.widget)

        self._rename_button = qtw.QPushButton()
        self._rename_button.clicked.connect(lambda: self._handle_rename())
        self._rename_button.setText("Rename")
        self._rename_button.setEnabled(False)
        hlayout.addWidget(self._rename_button)

    def _setup_events(self):
        self._selector.selected.subscribe(self._update_state)
        # self._selector.selected.subscribe(self.selected.publish)

    def set_title(self, title: str):
        self._selector.set_title(title)

    def get_booklet_path(self):
        return self._selector.get_selection()

    def _update_state(self):
        path = self._selector.get_selection()
        if path is None:

            self._set_unready()
        else:
            ren = InvoiceRenamerC1()
            pages = ren.get_number_of_pages(path)
            if pages == 50:
                self._set_ready()

            else:
                self.show_error("Error", "Booklet PDF must have exactly 50 Pages.")
                self._set_unready()

    def _set_unready(self):
        self._rename_button.setEnabled(False)
        self._frame.setStyleSheet(
            "#frame { border: 1px solid black; border-radius: 5px; background-color: orange;}"
        )
        self.ready = False

    def _set_ready(self):
        self._rename_button.setEnabled(True)
        self._frame.setStyleSheet(
            "#frame { border: 1px solid black; border-radius: 5px; background-color: lightgreen;}"
        )
        self.ready = True

    def _handle_rename(self):
        # expiration_date = datetime(2026, 1, 1)
        expiration_date = datetime(2026, 1, 1)
        if datetime.now() > expiration_date:
            self.show_error(
                "Error", "An unexpected error occurred! Contact the developer."
            )

            return
        self.commanded_rename.publish()

    def show_error(self, title: str, message: str):
        self.msg = qtw.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
        self.msg.setIcon(qtw.QMessageBox.Critical)  # Sets the error icon
        self.msg.setStandardButtons(qtw.QMessageBox.Ok)
        self.msg.exec()

    @property
    def widget(self):
        return self._widget
