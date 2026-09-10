import sys
import json
from client import CooleyTukeyFFT

def main():
    fft = CooleyTukeyFFT()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "fft":
            sig = [complex(v, 0) for v in params.get("signal", [])]
            X = fft.fft(sig)
            res = {"real": [val.real for val in X], "imag": [val.imag for val in X]}
        elif method == "ifft":
            sig = [complex(r, i) for r, i in zip(params.get("real", []), params.get("imag", []))]
            rec = fft.ifft(sig)
            res = {"real": [val.real for val in rec], "imag": [val.imag for val in rec]}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
