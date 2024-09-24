from order.order import Order


class TransactionLogger:
    def __init__(self):
        self.matches = []
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def log_match(self, order: Order):
        self.matches.append(order)
    
    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.notify(self.matches)



