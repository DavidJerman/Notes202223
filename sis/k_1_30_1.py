from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    Fvz = 15  # vzorčevalna frekvenca
    T = 2  # dolžina signala v sekundah
    t = np.arange(0, T, 1.0 / Fvz)  # časovni vektor

    f = 1.5  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f * t)

    # Spectral leakage
    Y = np.fft.fft(y)

    # Visualize
    fig, ax = plt.subplots(2, 1)

    ax[0].plot(t, y)
    ax[0].set_xlabel('Čas [s]')
    ax[0].set_ylabel('Amplituda')
    ax[0].set_title('Signal')

    ax[1].plot(np.abs(Y))
    ax[1].set_xlabel('Frekvenca [Hz]')
    ax[1].set_ylabel('Amplituda')
    ax[1].set_title('Spekter')

    plt.show()

    Fvz = 15  # vzorčevalna frekvenca
    T = 2  # dolžina signala v sekundah
    t = np.arange(0, T, 1.0 / Fvz)  # časovni vektor

    f = 1.6  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f * t)

    # Spectral leakage
    Y = np.fft.fft(y)

    # Visualize
    fig, ax = plt.subplots(2, 1)

    ax[0].plot(t, y)
    ax[0].set_xlabel('Čas [s]')
    ax[0].set_ylabel('Amplituda')
    ax[0].set_title('Signal')

    ax[1].plot(np.abs(Y))
    ax[1].set_xlabel('Frekvenca [Hz]')
    ax[1].set_ylabel('Amplituda')
    ax[1].set_title('Spekter')

    plt.show()

    Fvz = 15  # vzorčevalna frekvenca
    T = 2  # dolžina signala v sekundah
    t = np.arange(0, T, 1.0 / Fvz)  # časovni vektor

    f = 13  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f * t)

    # Spectral leakage
    Y = np.fft.fft(y)

    # Visualize
    fig, ax = plt.subplots(2, 1)

    ax[0].plot(t, y)
    ax[0].set_xlabel('Čas [s]')
    ax[0].set_ylabel('Amplituda')
    ax[0].set_title('Signal')

    ax[1].plot(np.abs(Y))
    ax[1].set_xlabel('Frekvenca [Hz]')
    ax[1].set_ylabel('Amplituda')
    ax[1].set_title('Spekter')

    plt.show()
