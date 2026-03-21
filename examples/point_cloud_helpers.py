import numpy as np

def generate_circle(n=30, noise=0.0):
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)
    points = np.column_stack((x, y))
    if noise > 0:
        points += noise * np.random.randn(*points.shape)
    return points
