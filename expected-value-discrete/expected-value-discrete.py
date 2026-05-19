import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x, copy=True, dtype=np.float64) 
    p = np.array(p, copy=True, dtype=np.float64)
    if abs(np.sum(p) - 1) > 1e-6:
        raise ValueError()
    return np.sum(x * p)
