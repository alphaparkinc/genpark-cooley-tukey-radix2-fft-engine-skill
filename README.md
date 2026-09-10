# genpark-cooley-tukey-radix2-fft-engine-skill

[![CI](https://github.com/alphaparkinc/genpark-cooley-tukey-radix2-fft-engine-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-cooley-tukey-radix2-fft-engine-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Cooley-Tukey Radix-2 Fast Fourier Transform (FFT) and Inverse FFT (IFFT) engine providing O(N log N) frequency domain decomposition.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / DSP Pipeline] -->|Input Signal| Engine[genpark-cooley-tukey-radix2-fft-engine-skill]
    Engine --> Transform[Frequency / Wavelet Decomposition]
    Transform --> Spectrum[(Spectral Representation)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Mathematically rigorous implementations of Fourier, Wavelet, Cosine, and Hilbert transforms.
- Native Model Context Protocol (MCP) server support for AI agent signal analysis.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-cooley-tukey-radix2-fft-engine-skill.git
cd genpark-cooley-tukey-radix2-fft-engine-skill
```

## Quickstart

```bash
python example_usage.py
```
