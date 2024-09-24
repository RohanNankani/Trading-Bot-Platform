from financial_instrument.financial_instrument import FinancialInstrument


class Equity(FinancialInstrument):
    def __init__(self, symbol, name, price=None, shares_outstanding=None):
        super().__init__(symbol, name)
        self.price = price
        self.shares_outstanding = shares_outstanding

    def get_value(self):
         return self.price

    def get_market_cap(self):
         return self.price * self.shares_outstanding

    def update_price(self, new_price):
         self.price = new_price

    def __repr__(self):
         return (f"Equity(symbol={self.symbol}, name={self.name}, "
                f"price={self.price}, shares_outstanding={self.shares_outstanding})")
