import click
import yaml
import importlib

from market.market import Market
from trading_bot.random_trader import RandomTrader

@click.command()
@click.option('-f', '--file', required=True, type=click.Path(exists=True), help='Path to the yaml config file')
def trade(file):

    with open(file, 'r') as yaml_config:
        config = yaml.safe_load(yaml_config)

    market_config = config['market']
    market = Market(
        matching_algorithm=market_config.get('matching_algorithm', 'fifo'),
        initial_price=market_config.get('initial_price', 100),
        time_steps=market_config.get('time_steps', 1000)
    )

    bots = []

    for bot_config in config['bots']:
       if bot_config['type'] == 'random':
           bot = RandomTrader(
               name=bot_config['name'],
               market=market,
               cash_balance=bot_config['cash_balance'],
               inventory=bot_config['inventory'],
               parameters=bot_config['parameters'],
               transaction_logger=market.transaction_logger
           )
           bots.append(bot) 
    

    total_time_steps = market.time_steps
    for timestep in range(total_time_steps):
        market.update_time()
        for bot in bots:
            bot.place_order()
        market.match_orders()
        market.notify()

    print("matches: ")
    print(market.transaction_logger.matches)

if __name__ == '__main__':
    trade()