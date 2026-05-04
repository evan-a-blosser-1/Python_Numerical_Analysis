import numpy as np

def sigmoid(x):
    """Sigmoid function

    Args:
        x (np.ndarray): input to the function

    Returns:
        np.ndarray: the sigmoid function of x
    """
    return 1 / (1 + np.exp(-x))