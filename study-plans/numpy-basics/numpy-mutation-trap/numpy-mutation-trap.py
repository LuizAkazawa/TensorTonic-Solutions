import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    row = np.asarray(data[row_idx], dtype=np.float64)
    ans = np.empty((2, len(row)), dtype=np.float64)
    ans[0] = row
    ans[1] = np.clip(row, lo, hi)
    return ans
    
    
    