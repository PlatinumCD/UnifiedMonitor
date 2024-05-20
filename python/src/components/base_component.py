from abc import ABC, abstractmethod

class BaseComponent(ABC):
    @abstractmethod
    def parse_data(self):
        pass

    @abstractmethod
    def print_component(self, stream):
        pass