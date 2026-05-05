import numpy as np

def create_filled_array(shape, kind):
    """
    Returns: 2D numpy array of given shape with dtype float64
    """
    a = shape[0]
    b = shape[1]
    if kind == "zeros":
        return np.zeros((a, b), dtype=float)
    else:
        return np.ones((a, b), dtype=float)