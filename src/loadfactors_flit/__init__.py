"""
A library for storing and calculating complete collections 
of load factors according to your local building code. 
"""

__version__ = "0.1.0"

from loadfactors_flit import loadfactors
from loadfactors_flit.loadfactors import (
    Load,
    open_load_combinations,
    factored_max,
    factored_min,
    factored_max_trace,
    factored_min_trace,
    get_factored_matrix,
    factor_load,
    alias_to_service_loads
)