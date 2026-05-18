import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    ans = np.array(data[row_start : row_stop], dtype=np.float64)
    bool_mask = np.where(ans > threshold)
    return ans[bool_mask]