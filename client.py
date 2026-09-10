import math
import cmath

class CooleyTukeyFFT:
    """
    Cooley-Tukey Radix-2 Fast Fourier Transform (FFT) Engine.
    Computes forward and inverse transforms for power-of-two sequences.
    """
    def fft(self, x):
        n = len(x)
        if n <= 1:
            return x
        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])
        t = [cmath.exp(-2j * math.pi * k / n) * odd[k] for k in range(n // 2)]
        return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]

    def ifft(self, x):
        n = len(x)
        x_conj = [z.conjugate() for z in x]
        transformed = self.fft(x_conj)
        return [z.conjugate() / n for z in transformed]
