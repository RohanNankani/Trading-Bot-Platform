import datetime
import random
from financial_instrument.equity import Equity
from market.market import Market
from matching_engine.match import Match
from order.order import Order
from trading_bot.trading_bot import TradingBot


class RandomTrader(TradingBot):
    def __init__(self, name,  market: Market, cash_balance, inventory, parameters, transaction_logger):
        super().__init__(name, market, cash_balance, inventory, parameters, transaction_logger)

    def place_order(self):
        volume = random.randint(1, self.inventory)
        price = volume * random.randint(1, int(self.cash_balance / volume))

        if price * volume > self.cash_balance:
            return

        order = Order(
            order_type=random.choice(['buy', 'sell']),
            price=price,
            volume=volume,
            timestamp=datetime.datetime.now(),
            financial_instrument=Equity('AAPL', 'Apple Inc.')
        )
        self.order_ids_placed.append(order.order_id)
        self.market.consume_order(order)
    
    def notify(self, matches: list[Match]):
        for match in matches[self.match_offset:]:
            if match.buyer_order_id in self.order_ids_placed:
                self.cash_balance -= match.price * match.volume
                self.inventory -= match.volume
            elif match.seller_order_id in self.order_ids_placed:
                self.cash_balance += match.price * match.volume
                self.inventory += match.volume
        self.match_offset = len(matches)
        print(self)

    def __str__(self):
        return f"Name: {self.name}, Cash Balance: {self.cash_balance}, Inventory: {self.inventory}, Parameters: {self.parameters}"