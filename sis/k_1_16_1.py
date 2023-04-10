from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Quantization example

    # Signal
    Fvz = 40  # vzorčevalna frekvenca
    T = 3  # dolžina signala v sekundah
    t = np.arange(0, T, 1.0 / Fvz)  # časovni vektor

    f1 = 5  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f1 * t)

    n = len(y)
    k = np.arange(n)

    # Quantization
    quantization_levels = 2 ** 4
    quantization_step = 2 / quantization_levels
    quantization_levels = np.arange(-1, 1, quantization_step)

    quantized_signal = np.zeros(n)
    for i in range(n):
        quantized_signal[i] = quantization_levels[np.argmin(np.abs(quantization_levels - y[i]))]
        quantized_signal[i] = quantized_signal[i] * 8

    # Visualize
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t, y)
    ax[0].set_xlabel('Čas [s]')
    ax[0].set_ylabel('Amplituda')
    ax[0].set_title('Signal')

    ax[1].scatter(t, quantized_signal)
    ax[1].set_xlabel('Čas [s]')
    ax[1].set_ylabel('Amplituda')
    ax[1].set_title('Kvantiziran signal')

    plt.show()
