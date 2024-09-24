class Match:
    def __init__(self, buyer_order_id, seller_order_id, volume, price, timestamp):
        self.buyer_order_id = buyer_order_id
        self.seller_order_id = seller_order_id
        self.volume = volume
        self.price = price
        self.timestamp = timestamp

    def __repr__(self):
        return (f"Match(buyer_order_id={self.buyer_order_id}, "
                f"seller_order_id={self.seller_order_id}, volume={self.volume}, "
                f"price={self.price}, timestamp={self.timestamp})")