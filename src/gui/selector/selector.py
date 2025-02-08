from abc import ABC, abstractmethod

from src.events.event import Event

import PyQt5.QtWidgets as qtw


class Selector(ABC):
    def __init_subclass__(cls, **kwargs):
        """Runs property validation when a subclass is created."""
        super().__init_subclass__(**kwargs)
        cls._validate_properties()

    @classmethod
    def _validate_properties(cls):
        """Checks if subclass properties override abstract properties correctly."""
        for name, value in cls.__dict__.items():
            if cls._is_abstract_property(name):
                cls._ensure_property(name, value)

    @classmethod
    def _is_abstract_property(cls, name):
        """Checks if a given attribute is an abstract property in the base classes."""
        return any(
            hasattr(base, name) and isinstance(getattr(base, name), property)
            for base in cls.__bases__
        )

    @classmethod
    def _ensure_property(cls, name, value):
        """Raises an error if the subclass does not define the property correctly."""
        if not isinstance(value, property):
            raise TypeError(
                f"Class '{cls.__name__}' must define '{name}' as a property."
            )

    @property
    @abstractmethod
    def widget(self) -> qtw.QWidget: ...

    @property
    @abstractmethod
    def selected(self) -> Event: ...

    @abstractmethod
    def get_selection(self) -> str: ...

    @abstractmethod
    def set_title(self, title: str) -> None: ...

    @abstractmethod
    def set_file_types(self, *extensions: str) -> None: ...
