class Observer:
    def update(self, evento):
        raise NotImplementedError


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify_observers(self, evento):
        for observer in self._observers:
            observer.update(evento)
