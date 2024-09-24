from data_source.data_source import DataSource
from order.order_loader import OrderLoader

class OrderBook:
    def __init__(self):
        self.bids = []  # list of buy orders
        self.asks = []  # list of sell orders
        self.orders = []

    def load_orders(self):
        self.orders = self.order_loader.load_orders()
        for order in self.orders:
            if order.order_type == 'buy':
                self.bids.append(order)
                self.bids = sorted(self.bids, key=lambda x: (-x.price, x.timestamp))
            elif order.order_type == 'sell':
                self.asks.append(order)
                self.asks = sorted(self.asks, key=lambda x: (x.price, x.timestamp))

    def consume_order(self, order):
        self.orders.append(order)
        if order.order_type == 'buy':
            self.bids.append(order)
        elif order.order_type == 'sell':
            self.asks.append(order)
    
    def get_bids(self):
        return sorted(self.bids, key=lambda x: (x.timestamp))
    
    def get_asks(self):
        return sorted(self.asks, key=lambda x: (x.timestamp))

    def get_orders(self):
        return sorted(self.order, key=lambda x: (x.timestamp))