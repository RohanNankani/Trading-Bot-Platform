from abc import ABC, abstractmethod

class FinancialInstrument(ABC):
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    @abstractmethod
    def get_value(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(symbol={self.symbol}, name={self.name})"
