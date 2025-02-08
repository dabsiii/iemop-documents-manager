from src.events.event import Event


class Event_(Event):

    def __init__(self):
        self._functions = []

    def subscribe(self, function) -> None:
        self._functions.append(function)

    def publish(self, data=None) -> None:
        if data is not None:
            [function(data) for function in self._functions]

        if data is None:
            [function() for function in self._functions]
