import csv
from data_source.data_source import DataSource
from financial_instrument.equity import Equity
from financial_instrument.financial_instrument import FinancialInstrument
from order.order import Order


class OrderLoader:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def load_orders(self) -> 'list[Order]':
        orders = []
        for data in self.data_source.load_data():
            financial_instrument_type = data['asset_class']
            financial_instrument = None

            if financial_instrument_type.lower() == 'equity':
                financial_instrument = Equity(
                    symbol=data['financial_instrument_symbol'],
                    name=data['financial_instrument_name'],
                    price=float(data['price']),
                    shares_outstanding=int(data['volume'])
                )
            else:
                raise ValueError(f"Unsupported financial instrument type: {financial_instrument_type}")
            
            order = Order(
                order_type=data['order_type'],
                price=float(data['price']),
                volume=int(data['volume']),
                timestamp=int(data['timestamp']),
                financial_instrument=financial_instrument
            )
            orders.append(order)
        return orders
