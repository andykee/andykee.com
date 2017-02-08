Title: Power Spectral Density 
Date: 2015-12-23
Category: eng 
Tags: matlab, signal processing
Summary: 
Slug: power-spectral-density 
Authors: AK
Status: draft

Power spectral density (PSD) shows the power of a time series signal in each frequency band. Think of looking at a PSD plot like looking at time series data plotted as a function of frequency, rather than time. In practice, the PSD is computed as the absolute magnitude of the Fourier transform squared. For example, given a signal $x(n)$ and its DFT $X(f)$, then the absolute magnitude if the DFT is $|X(f)|$ and the PSD is $|X(f)|^2$.

Suppose that we have $N$ samples in out time series data $x(n)$ with the samples equally spaced by $\Delta t$. Since the PSD is given as the modulus squared of $X(f)$, we have

$$S(f) = \frac{\Delta t}{N}\left| \sum_{n=0}^{N-1}x(n)e^{-i2\pi nf}\right|^2 \hspace{1em} , \hspace{1em} -\frac{1}{2\Delta t} < f \leq \frac{1}{2\Delta t}$$

where $1/(2\Delta t)$ is the Nyquist frequency. 

The PSD has units of energy per frequency and thus can be used to compute the net power of a process by integrating over frequency:

$$P_{net} = 2\int_0^\infty S(f)df$$

### Computing the PSD in MATLAB
The simplest way to compute the PSD of time series data in MATLAB is to use `periodogram` in the Signal Processing Toolbox. Given a signal `x` with a sampling frequency `fs`, the PSD is

    :::matlab
    [pxx, f] = periodogram(x,[],length(x),fs);
    semilogx(f, 10*log10(pxx))

In the absence of the Signal Processing Toolbox, it is also possible to compute [PSD estimates using FFT](http://www.mathworks.com/help/signal/ug/psd-estimate-using-fft.html).

That being said, using the periodogram to compute the PSD is one of the worst methods available. Many other methods exist, with my personal favorite being Welch's method. Again given a signal `x` with a sampling frequency `fs`, the PSD is

    :::matlab
    window = 512;
    fs = 1000;
    [pxx,f] = pwelch(x,window,[],[],fs);
    semilogx(f, 10*log10(pxx))
    % loglog(f,pxx)


