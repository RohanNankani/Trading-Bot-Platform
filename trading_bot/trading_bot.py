from abc import ABC, abstractmethod

from market.market import Market


class TradingBot(ABC):
    def __init__(self, name, market: Market, cash_balance, inventory, parameters, transaction_logger):
        self.name = name
        self.market = market
        self.cash_balance = cash_balance
        self.inventory = inventory
        self.parameters = parameters
        self.init_inventory = inventory
        self.init_balance = cash_balance
        self.transaction_logger = transaction_logger
        self.match_offset = 0
        self.order_ids_placed = []

    @abstractmethod
    def place_order(self):
        raise NotImplementedError

    def notify(self, matches):
        pass