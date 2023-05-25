from loadfactors import open_load_combinations, factored_max, Load
import pathlib
import numpy as np

NBCC_COMBOS = open_load_combinations(
    pathlib.Path(__file__).parents[1] / 'src' / 'loadfactors' / 'NBCC_15.json'
    )

L0 = Load() # An empty load
L1 = Load(D=2.3, L=2.4, S=0.9) # Not all fields need be entered
L2 = Load( # A load with array values
    D=np.array([0.6, 1.1, 0.4]), 
    L=np.array([2.4, 3.6, 0.8]),
    S=np.array([0.5, 1.2, 3.6]),
    W=np.zeros(3),
    E=np.zeros(3),
)

def test_max_factored():
    assert factored_max(L1, NBCC_COMBOS) == 7.375