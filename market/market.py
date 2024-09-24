from logger.transaction_logger import TransactionLogger
from matching_engine.matching_engine import MatchingEngine
from order.order_book import OrderBook
from logger.logging_config import logger


class Market:
    def __init__(self, matching_algorithm=None, initial_price=1000, time_steps=1000):
        self.transaction_logger = TransactionLogger()

        self.machine_engine = MatchingEngine(matching_algorithm, self.transaction_logger)
        self.initial_price = initial_price
        self.time_steps = time_steps
        self.current_time = 0
        
        self.order_book = OrderBook()
    
    def update_time(self):
        self.current_time += 1

    def match_orders(self):
        logger.info("Starting to match orders")
        self.machine_engine.match_orders(self.order_book.get_bids(), self.order_book.get_asks())
        logger.info("Order matching completed")
    
    def notify(self):
        logger.info("Notifying all subscribers")
        self.transaction_logger.notify_subscribers()

    def consume_order(self, order):
        self.order_book.consume_order(order)