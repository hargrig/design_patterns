# Observer pattern is used when there is one-to-many relationship between objects 
# such as if one object is modified, its depenedent objects 
# are to be notified automatically. 
# Observer pattern falls under behavioral pattern category.


from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject:
    def __init__(self, state):
        self._state = state
        self.observers: Observer = []

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify_to_observers()

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_to_observers(self):
        for observer in self.observers:
            observer.update()


class BinaryObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"Binary String: {format(self.subject.state, 'b')}" )

class OctalObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"Octal String: {oct(self.subject.state)}")

class HexaObserver(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"Hex String: {hex(self.subject.state)}")


class DemoObserverPattern:
    def main(self):
        subject = Subject(None)

        # Subscriptions
        HexaObserver(subject)
        OctalObserver(subject)
        BinaryObserver(subject)

        print("First state change: 15")
        subject.state = 15

        print("------------------------------------")

        print("Second state change: 16")
        subject.state = 16


if __name__ == "__main__":
    demo = DemoObserverPattern()
    demo.main()