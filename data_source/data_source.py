from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def load_data(self):
        pass