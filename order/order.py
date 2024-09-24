from datetime import timezone, datetime


class Order:
    _id_counter = 1
    
    def __init__(self, order_type, price, volume, timestamp, financial_instrument):
        self.order_id = Order._id_counter
        Order._id_counter += 1
        self.order_type = order_type
        self.price = price
        self.volume = volume
        self.timestamp = self._convert_to_utc(timestamp)
        self.financial_instrument = financial_instrument

    def _convert_to_utc(self, timestamp):
        if isinstance(timestamp, int):
            timestamp = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        elif timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)
        return timestamp.astimezone(timezone.utc)

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, order_type={self.order_type}, price={self.price}, "
                f"volume={self.volume}, timestamp={self.timestamp}, financial_instrument={self.financial_instrument})")

    def execute(self, matched_volume):
        self.volume -= matched_volume

        if self.volume == 0:
            print(f"Order {self.order_id} is fully executed.")
        else:
            print(f"Order {self.order_id} is partially executed. Remaining volume: {self.volume}")

    def is_fully_executed(self):
        return self.volume == 0