import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

import sys
from src.gui.selector.selector_c1 import SelectorC1
from pathlib import Path

from icecream import ic


from src.events.event_ import Event_, Event


from src.gui.booklet_gui.booklet_gui import BookletGui

from typing import List


class Home:
    def __init__(self):

        # self._init_ui()
        # self._setup_events()
        self._selected_tracking_data = Event_()
        self._tracker_data_path: str = None

    def _init_ui(self):
        self._widget = qtw.QWidget()
        self._widget.setWindowTitle("Invoice Renamer")
        self._widget.resize(500, 600)
        layout = qtw.QVBoxLayout()
        self._widget.setLayout(layout)

        self._tracking_data_selector = SelectorC1()
        self._tracking_data_selector.set_title("Tracking Data (csv)")
        self._tracking_data_selector.set_file_types("csv")
        layout.addWidget(self._tracking_data_selector.widget)

        self._scroll_area = qtw.QScrollArea()
        scroll_widget = qtw.QWidget()
        self._scroll_area.setWidget(scroll_widget)
        # self._scroll_area.setStyleSheet("QScrollArea { background-color: red; }")
        self._scroll_area.setWidgetResizable(True)
        layout.addWidget(self._scroll_area)

        rename_button = qtw.QPushButton()
        rename_button.setText("Multiple Rename")
        layout.addWidget(rename_button)

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

    def display_on_scroll(self, widgets: List[qtw.QWidget]) -> None:
        self.clear_scroll()

        scroll_widget = qtw.QWidget()
        scroll_layout = qtw.QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        self._scroll_area.setWidget(scroll_widget)  # Set the new widget

        for widget in widgets:
            scroll_layout.addWidget(widget)

    def clear_scroll(self):
        old_widget = self._scroll_area.widget()  # Get the current widget
        if old_widget is not None:
            old_widget.setParent(None)  # Detach from scroll area
            old_widget.deleteLater()  # Delete to free memory

    def display_invalid_tracker_data_file(self):
        self.clear_scroll()
        scroll_widget = qtw.QWidget()
        scroll_layout = qtw.QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        self._scroll_area.setWidget(scroll_widget)  # Set the new widget

        label = qtw.QLabel()
        label.setText("Invalid Tracker Data File.")

        label.setAlignment(qtc.Qt.AlignCenter)

        # Set red text color using stylesheets
        label.setStyleSheet("color: red; font-size: 20px; font-weight: bold;")

        scroll_layout.addWidget(label)

    def _set_tracker_data_path(self):
        self._tracker_data_path = self._tracking_data_selector.get_selection()

    def show(self):
        app = qtw.QApplication(sys.argv)
        self._init_ui()
        self._setup_events()
        self._widget.show()
        sys.exit(app.exec_())
