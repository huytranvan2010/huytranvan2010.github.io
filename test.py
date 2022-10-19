import numpy as np

def softmax_grad(s):    # truyền vào array softmax
    # s truyền vào là 1d-numpy array (n,)
    s_new = s.reshape((1, -1))
    jacobi = np.diag(s) - np.dot(s_new.T, s_new)
    return jacobi

s = np.array([0.5, 0.5])

print(softmax_grad(s))