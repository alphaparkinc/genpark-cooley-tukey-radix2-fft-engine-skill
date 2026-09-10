from client import CooleyTukeyFFT

def main():
    print("=== Testing Cooley-Tukey Radix-2 FFT Engine ===")
    fft = CooleyTukeyFFT()
    sig = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0]
    X = fft.fft([complex(v, 0) for v in sig])
    print("FFT output magnitude:", [round(abs(val), 3) for val in X])
    recon = fft.ifft(X)
    print("Reconstructed real part:", [round(r.real, 3) for r in recon])

    for orig, r in zip(sig, recon):
        assert abs(orig - r.real) < 1e-6
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
