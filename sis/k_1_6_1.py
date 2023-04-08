from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    Fvz = 40  # vzorčevalna frekvenca
    T = 3  # dolžina signala v sekundah
    t1 = np.arange(0, T, 1.0 / Fvz)  # časovni vektor
    t2 = np.arange(0, T / 2, 1.0 / Fvz)  # časovni vektor

    f1 = 5  # frekvenca sinusoide
    f2 = 7  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f1 * t1)
    y[0:len(t2)] = y[0:len(t2)] + 0.5 * np.sin(2 * np.pi * f2 * t2)

    n = len(y)
    k = np.arange(n)

    frq = k / T  # celotno frekvenčno območje

    Y = np.fft.fft(y) / n  # izračun fft in normalizacija

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t1, y)
    ax[0].set_xlabel('Čas [s]')
    ax[0].set_ylabel('Amplituda')
    ax[0].set_title('Signal')

    ax[1].plot(frq, abs(Y), 'r')  # izris spektra
    ax[1].set_xlabel('Frekvenca [Hz]')
    ax[1].set_ylabel('|Y(f)|')
    ax[1].set_title('Spekter')

    plt.show()

    real = np.real(Y)
    imag = np.imag(Y)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(frq, real, 'r')  # izris spektra
    ax[0].set_xlabel('Frekvenca [Hz]')
    ax[0].set_ylabel('Re(Y(f))')

    ax[1].plot(frq, imag, 'r')  # izris spektra
    ax[1].set_xlabel('Frekvenca [Hz]')
    ax[1].set_ylabel('Im(Y(f))')

    plt.show()

    Fvz = 40  # vzorčevalna frekvenca
    T = 3  # dolžina signala v sekundah
    t = np.arange(0, T, 1.0 / Fvz)  # časovni vektor

    f = 5  # frekvenca sinusoide

    y = np.sin(2 * np.pi * f * t + np.pi / 4)

    n = len(y)
    k = np.arange(n)

    frq = k / T  # celotno frekvenčno območje

    Y = np.fft.fft(y) / n  # izračun fft in normalizacija

    real = np.real(Y)
    imag = np.imag(Y)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(frq, real, 'r')  # izris spektra
    ax[0].set_ylabel('Re(Y(f))')

    ax[1].plot(frq, imag, 'r')  # izris spektra
    ax[1].set_ylabel('Im(Y(f))')

    plt.show()
