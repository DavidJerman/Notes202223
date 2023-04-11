from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    Fvz = 80
    T = 1
    t = np.arange(0, T, 1.0 / Fvz)

    f1 = 5
    f2 = 75

    y1 = np.sin(2 * np.pi * f1 * t)
    y2 = np.sin(2 * np.pi * f2 * t)
    y12 = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    plt.plot(t, y1, 'r')
    plt.plot(t, y2, 'g')
    plt.plot(t, y12, 'b')
    plt.legend(['f1', 'f2', 'f1+f2'])
    plt.show()

    Fvz = 320
    T = 1
    t = np.arange(0, T, 1.0 / Fvz)

    f1 = 5
    f2 = 75

    y = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    plt.plot(t, y, 'b')
    plt.show()

