import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    data = np.asarray(data, dtype=np.float64)
    mask = data > threshold
    
    mask_layer = mask.astype(np.float64)
    
    has_any = mask.any(axis=1, keepdims=True)
    any_ans = np.where(has_any, data, 0.0)
    
    has_all = mask.all(axis=1, keepdims=True)
    all_ans = np.where(has_all, data, 0.0)
    
    return np.stack([mask_layer, any_ans, all_ans])