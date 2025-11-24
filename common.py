import numpy as np

## Standard Sinusoid
# t = time              | seconds
# A = amplitude         | scalar
# f = frequency         | cycles per second
# phi = phase/offset    | radians
def x(t, A = 1, f = 44100, phi = 0):
    return A * np.cos(2 * np.pi * f * t + phi)

