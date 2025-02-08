import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


import sys
from src.gui.selector.selector_c1 import SelectorC1
from pathlib import Path

from icecream import ic


from src.events.event_ import Event_, Event


class Home:
    def __init__(self):

        # self._init_ui()
        # self._setup_events()
        self._selected_tracking_data = Event_()
        self._tracker_data_path: str = None

    def _init_ui(self):
        self._widget = qtw.QWidget()
        layout = qtw.QHBoxLayout()
        self._widget.setLayout(layout)

        self._tracking_data_selector = SelectorC1()
        self._tracking_data_selector.set_title("Tracking Data (csv)")
        self._tracking_data_selector.set_file_types("csv")
        layout.addWidget(self._tracking_data_selector.widget)

    def _setup_events(self):

        self._tracking_data_selector.selected.subscribe(self._set_tracker_data_path)
        self._tracking_data_selector.selected.subscribe(
            self._selected_tracking_data.publish
        )

    @property
    def selected_tracking_data(self) -> Event:
        return self._selected_tracking_data

    def get_tracker_data_path(self) -> str:
        return self._tracker_data_path

    def _set_tracker_data_path(self):
        self._tracker_data_path = self._tracking_data_selector.get_selection()

    def show(self):
        app = qtw.QApplication(sys.argv)
        self._init_ui()
        self._setup_events()
        self._widget.show()
        sys.exit(app.exec_())
