from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    freq = 3
    A = 1.5
    phase = 0.5 * np.pi  # pi
    sampling_freq = 40
    T = 1

    x = np.linspace(0, T, T * sampling_freq)
    y = A * np.sin(2 * np.pi * freq * x + phase)

    plt.plot(x, y)
    plt.xlabel('x [t]')
    plt.show()

    freq = 4.5
    A = 1.4
    phase = 1.25 * np.pi  # pi
    sampling_freq = 60
    T = 1.5

    x = np.linspace(0, T, int(T * sampling_freq))
    y = A * np.sin(2 * np.pi * freq * x + phase)

    plt.plot(x, y)
    plt.xlabel('x [t]')
    plt.show()
