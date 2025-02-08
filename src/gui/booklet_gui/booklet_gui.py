import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


import sys
from src.gui.selector.selector_c1 import SelectorC1
from pathlib import Path

from icecream import ic


from src.events.event_ import Event_, Event


class BookletGui:
    def __init__(self):
        self._init_ui()
        self._setup_events()

    def _init_ui(self):
        self._widget = qtw.QWidget()
        widget_layout = qtw.QVBoxLayout()
        self._widget.setLayout(widget_layout)

        frame = qtw.QFrame()
        frame.setObjectName("frame")

        frame.setStyleSheet("#frame { border: 1px solid black; border-radius: 5px; }")
        frame_layout = qtw.QVBoxLayout()
        frame.setLayout(frame_layout)
        widget_layout.addWidget(frame)

        hlayout = qtw.QHBoxLayout()
        frame_layout.addLayout(hlayout)

        self._selector = SelectorC1()
        hlayout.addWidget(self._selector.widget)

        rename_button = qtw.QPushButton()
        rename_button.clicked.connect(lambda: self._handle_rename())
        rename_button.setText("Rename")
        hlayout.addWidget(rename_button)

    def set_title(self, title: str):
        self._selector.set_title(title)

    def _setup_events(self):
        pass

    def _handle_rename(self):
        print("indide handle rename")

    @property
    def widget(self):
        return self._widget
