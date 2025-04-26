#!/usr/bin/env python3

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/tmp/algorithm_debug.log"),  # Log to file
        logging.StreamHandler()                      # Also log to console
    ]
)

from utils.sorting_algorithms import SortingAlgorithms
from utils.searching_algorithms import SearchingAlgorithms
from utils.graph_algorithms import GraphAlgorithms
from utils.dynamic_programming import DynamicProgramming
from utils.string_algorithms import StringAlgorithms
from utils.data_structures import DataStructures
from utils.math_algorithms import MathAlgorithms
from utils.greedy_algorithms import GreedyAlgorithms
from utils.backtracking_algorithms import BacktrackingAlgorithms
from utils.divide_and_conquer_algorithms import DivideAndConquerAlgorithms
from utils.misc_algorithms import MiscAlgorithms

def main():
    ''' Run each test '''
    completed_all_successfully = True
    algorithm_classes = [
        ("SortingAlgorithms", SortingAlgorithms),
        ("SearchingAlgorithms", SearchingAlgorithms),
        ("GraphAlgorithms", GraphAlgorithms),
        ("DynamicProgramming", DynamicProgramming),
        ("StringAlgorithms", StringAlgorithms),
        ("DataStructures", DataStructures),
        ("MathAlgorithms", MathAlgorithms),
        ("GreedyAlgorithms", GreedyAlgorithms),
        ("BacktrackingAlgorithms", BacktrackingAlgorithms),
        ("DivideAndConquerAlgorithms", DivideAndConquerAlgorithms),
        ("MiscAlgorithms", MiscAlgorithms)
    ]
    
    for name, algorithm_class in algorithm_classes:
        logging.info("Starting {} tests.".format(name))
        try:
            algorithm_class.main()
            logging.info("{} tests completed successfully.".format(name))
        except Exception as e:
            completed_all_successfully = False
            logging.error("Error in {}: {}".format(name, e), exc_info=True)
        print('\n\n', end="")
    
    if completed_all_successfully:
        logging.info("\nALL tests completed successfully!")

if __name__ == "__main__":
    main()

