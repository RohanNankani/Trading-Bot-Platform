from abc import ABC, abstractmethod
from datetime import datetime
from logger.logging_config import logger
from logger.transaction_logger import TransactionLogger
from matching_engine.match import Match
from order.order import Order

class MatchingAlgorithm(ABC):
	@abstractmethod
	def match_order(self, order_book, order):
		pass

class BaseMatchingAlgorithm:
	def match(self, bids, asks):
		raise NotImplementedError()

class FIFOAlgorithm(BaseMatchingAlgorithm):

	def __init__(self, transaction_logger: TransactionLogger):
		self.transaction_logger = transaction_logger
		
	def match(self, bids: Order, asks: Order):
		logger.info("Starting FIFO matching algorithm")
		
		while bids and asks:
			highest_bid = bids[0]
			lowest_ask = asks[0]
			logger.info("Matching bid: %s with ask: %s", highest_bid, lowest_ask)
			
			if highest_bid.price >= lowest_ask.price:
				matched_volume = min(highest_bid.volume, lowest_ask.volume)
				
				highest_bid.volume -= matched_volume
				lowest_ask.volume -= matched_volume
				logger.info("Matched volume: %s", matched_volume)

				self.transaction_logger.log_match(Match(highest_bid.id, lowest_ask.id, matched_volume, highest_bid.price, datetime.now()))
				
				if highest_bid.volume == 0:
					bids.pop(0)
					logger.info("Bid fully matched and removed: %s", highest_bid)
				
				if lowest_ask.volume == 0:
					asks.pop(0)
					logger.info("Ask fully matched and removed: %s", lowest_ask)
			else:
				logger.info("No match found")
				break
		
		logger.info("FIFO matching algorithm completed")

class ProRataAlgorithm(BaseMatchingAlgorithm):
	def __init__(self, transaction_logger: TransactionLogger):
		self.transaction_logger = transaction_logger

	def match(self, bids, asks):
		"""
		Implements the Pro Rata matching algorithm.
		This algorithm matches orders based on the proportion of the ask volume to the total ask volume.
		It distributes the bid volume across multiple asks proportionally.
		"""
		logger.info("Starting Pro Rata matching algorithm")
		
		total_volume = sum(o.volume for o in asks)
		logger.info("Total ask volume: %s", total_volume)
		
		for bid in bids:
			for ask in asks:
				if bid.price >= ask.price:
					matched_volume = (ask.volume / total_volume) * bid.volume
					matched_volume = min(matched_volume, ask.volume)
					logger.info("Matched volume: %s", matched_volume)
					self.transaction_logger.log_match(Match(bid.order_id, ask.order_id, matched_volume, bid.price, datetime.now()))
	