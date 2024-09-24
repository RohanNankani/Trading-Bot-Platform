from logger.transaction_logger import TransactionLogger
from matching_engine.matching_algorithms import FIFOAlgorithm, ProRataAlgorithm


class MatchingEngine:
    
    def __init__(self, matching_algorithm, logger: TransactionLogger):
        """Initialize the matching engine with a matching algorithm."""
        self.matching_algorithm = self._create_matching_algorithm(matching_algorithm, logger)

    def _create_matching_algorithm(self, algorithm_name, logger):
        """Create an instance of the matching algorithm based on the algorithm name."""
        if algorithm_name == "fifo":
            return FIFOAlgorithm(logger)
        elif algorithm_name == "prorata":
            return ProRataAlgorithm(logger)
        else:
            raise ValueError(f"Unknown matching algorithm: {algorithm_name}")
   
    def match_orders(self, bids, asks):
        """Match orders in the matching engine."""
        self.matching_algorithm.match(bids, asks)