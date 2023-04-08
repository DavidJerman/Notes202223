from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    freq = 3
    A = 1.5
    phase = 0.5 * np.pi  # pi

    x = np.linspace(0, 4, 200)
    y = A * np.sin(np.pi * freq * x + phase)

    plt.plot(x, y)
    plt.xlabel('x (pi)')
    plt.show()
