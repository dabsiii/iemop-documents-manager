import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


from src.events.event_ import Event_
from src.gui.selector.selector import Selector
from pathlib import Path


class SelectorC1(Selector):

    def __init__(self):
        self._title = "Title"
        self._button_text = "Choose File"
        self._filename = "no selection"
        self._file_types = "All Files (*);;Text Files (*.txt)"
        self._file_path = None

        self._init_ui()
        self._setup_events()

    def _init_ui(self):
        """
        # 0 Widget
        # 0.1 _WidgetLayout
        # 0.1.1 _Frame
        # 0.1.1 _Frame Layout (V)
        # 0.1.1.1 _Title Label
        # 0.1.1.1.2 _Horizontal Layout
        # 0.1.1.1.2.1 _Choose File PushButton
        # 0.1.1.1.2.2 _Filepath LineEdit
        # 0.1.1.1.3 _Filename Label
        """
        # 0 Widget
        self._widget = qtw.QWidget()
        # 0.1 _WidgetLayout
        widget_layout = qtw.QVBoxLayout()
        self._widget.setLayout(widget_layout)

        # 0.1.1 _Frame
        frame = qtw.QFrame()
        widget_layout.addWidget(frame)
        # 0.1.1 _Frame Layout (V)
        frame_layout = qtw.QVBoxLayout()
        frame.setLayout(frame_layout)

        # 0.1.1.1 _Title Label
        self._title_label = qtw.QLabel()
        self._title_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        self._title_label.setText(self._title)
        frame_layout.addWidget(self._title_label)

        # 0.1.1.1.2 _Horizontal Layout
        horizontal_layout = qtw.QHBoxLayout()
        frame_layout.addLayout(horizontal_layout)

        # 0.1.1.1.2.1 _Choose File PushButton
        self._choose_file_button = qtw.QPushButton()
        self._choose_file_button.setText(self._button_text)
        horizontal_layout.addWidget(self._choose_file_button)

        # 0.1.1.1.2.2 _Filepath LineEdit
        self._file_path_line_edit = qtw.QLineEdit()
        horizontal_layout.addWidget(self._file_path_line_edit)

        # 0.1.1.1.3 _Filename Label
        self._file_name_label = qtw.QLabel()
        self._file_name_label.setText(self._filename)
        self._file_name_label.setAlignment(qtc.Qt.AlignCenter)
        frame_layout.addWidget(self._file_name_label)

    def _setup_events(self):
        self._selected = Event_()
        self._selected.subscribe(self._update_file_path_display)
        self._selected.subscribe(self._update_file_name_display)

        self._choose_file_button.clicked.connect(self._open_file_dialog)

    @property
    def selected(self) -> Event_:
        return self._selected

    @property
    def widget(self) -> qtw.QWidget:
        return self._widget

    def get_selection(self) -> str:
        return self._file_path

    def set_title(self, title: str) -> None:
        self._title_label.setText(title)

    def set_file_types(self, *extensions) -> None:
        self._file_types = f"(*.{' *.'.join(extensions)})"

    def _open_file_dialog(self) -> None:
        file_path, _ = qtw.QFileDialog.getOpenFileName(
            self.widget, "Open File", "", self._file_types
        )

        self._file_path = file_path or None
        self._selected.publish()

    def _update_file_path_display(self) -> None:
        if self._file_path:
            self._file_path_line_edit.setText(self._file_path)
        else:
            self._file_path_line_edit.setText("")

    def _update_file_name_display(self) -> None:
        if self._file_path:
            path = Path(self._file_path)
            self._file_name_label.setText(path.name)
        else:
            self._file_name_label.setText("no selection")
