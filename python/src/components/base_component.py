from abc import ABC, abstractmethod

class BaseComponent(ABC):
    @abstractmethod
    def parse_data(self):
        pass

    @abstractmethod
    def print_component(self, stream):
        pass

    @abstractmethod
    def record_component(self, csv_writer):
        pass