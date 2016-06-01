Title: Verifying simulated PSFs represent proper detector sampling
Date: 2016-02-05
Category: wfsc
Tags: matlab, optics
Summary: 
Slug: psf-on-fpa-sampling
Authors: AK

There's been a lot of discussion about this at work lately. We have a fairly robust MATLAB function to create simulated PSFs for an optical system given a geometric pupil, an amplitude map of the pupil, an OPD map, filter bandpass, and desired sampling of the resulting PSF. While it's fairly straightforward to generate a PSF for an arbitrary system and OPD, the nagging worry that the simulated PSF isn't a correct representation of what the optical system we're simulating would actually produce always remains. The issue always comes back to how to correctly set up the sampling. While I won't go in to the specifics of how to do that using our MATLAB function here, I will present a simple sanity check based on first principles that allows for easy validation that simulated PSFs are in fact being represented in native detector sampling.

## Physical Size of an Airy disk on a detector
The PSF of a diffraction-limited optical system with a circular aperture is the Airy disk. The angular radius of an Airy disk (from center to its first minima) is given by:

$$\begin{equation}\sin{\theta} = 1.22\displaystyle\frac{\lambda}{D}\end{equation}$$
 
where $\theta$ is the angular resolution in radians, $\lambda$ is the wavelength (or average wavelength) of light in meters, and $D$ is the aperture diameter in meters. Typically the small angle approximation is invoked because $\theta$ is very small, allowing us to rewrite (1) as: 

$$\theta = 1.22 \displaystyle\frac{\lambda}{D}$$

In this case however, it is more useful to consider the physical meaning of $\sin{\theta}$ which for our optical system is the ratio of the distance to the first minima of the Airy disk to the distance from the aperture to the detector (see Fig. 1). With this relation in hand, and assuming the distance from the aperture to the detector can be approximated by the focal length of the optical system, we rewrite (1) as:

$$\displaystyle\frac{x}{f} = 1.22\displaystyle\frac{\lambda}{D}$$

After a little rearranging and noting that F-number is $F = \frac{f}{D}$ we have an expression for the linear distance to the first minima of an Airy disk. For our purposes, it is most convenient to represent this in terms of diameter: 

$$\begin{equation}x = 2.44\lambda F\end{equation}$$

It is also worth mentioning that the above calculation forms the basis of the [Rayleigh criterion](https://en.wikipedia.org/wiki/Angular_resolution#Explanation) 

### Airy Disk FWHM
Because of the way sampled imaging systems work, we'll get a more accurate result if we use a measurement of the Full Width at Half Maximum (FWHM) of the Airy disk to validate our simulated results. For an Airy disk, the power is 50% of max at:

$$\mbox{HWHM} = 0.514\displaystyle\frac{\lambda}{D}$$

so the (angular) FWHM is

$$\mbox{FWHM} = 1.028\displaystyle\frac{\lambda}{D}$$

Repeating the rearranging from above, we have the (spatial) FWHM as:

$$\begin{equation}\mbox{FWHM} = 1.028\lambda F\end{equation}$$

We now have expressions for the size of an Airy disk (to its first minima) and its FWHM. Next we'll look at how a detector captures the resulting image.

### Detector Resolution
Up to this point we've only discussed the elements of an optical system leading up to our detetor. We've assumed our system is diffraction limited so we're presenting an "ideal" image to the detector. The detector samples this (continuous) image by collecting incoming photons on a grid of pixels to produce a discrete signal. It is at this point the pixel size finally becomes important.

To find the number of pixels under the FWHM we simply divide (3) by our pixel size:

$$\begin{equation}\mbox{N}_{\mbox{px}} = \displaystyle \frac{1.028\lambda F}{d}\end{equation}$$

## Checking our results in MATLAB
Now that we have an expression for the number of pixels we expect to see on our detector at the FWHM of an Airy disk let's see if our simulated PSFs are correctly sized. We'll increase the sampling by a factor of 10 to give a more accurate measurement - we just need to remember to scale the expected number of pixels at the FWHM accordingly. First, let's calculate the expected number of pixels under the FWHM of an Airy disk for our system:

    :::matlab
    lambda = 650e-9;
    f_number = 16.8;
    px_size = 5e-6;

    npx_calc = (1.028*lambda*f_number)/px_size; 

On the real system we expect to see 2.24 pixels under the FWHM of the Airy disk, but because we'll increase the sampling by a factor of 10, we'll really be looking for 22.4 pixels. 

Next, let's simulate a PSF for our system in an unabberated state:

![PSF and FWHM Mask]({filename}/img/psf-fwhm.png)

A simple bit of MATLAB code calculates the FWHM and counts the number of pixels at the FWHM of the simulated PSF:

    :::matlab
    psf = psf./(max(max(psf)));  % normalize the PSF
    fwhm = psf > 0.5;            % create a binary mask of the PSF
    [r,c] = find(fwhm);          % extract only the nonzero elements

    nr = max(r) - min(r);
    nc = max(c) - min(c);

    npix_meas = max([nr nc]);
    
From the figure above, we confirm the number of pixels under the FWHM of the simulated PSF is 22, so our PSF is being correctly represented by our simulation.

## (Update) A simple check using Q
Q represents the ratio between the resolving power of an optical system and the sampling ability of a detector.

$$\begin{equation}Q = \displaystyle \frac{\lambda F}{d}\end{equation}$$

A system with $Q = 2$ is considered to be "well sampled". We see from above that the number of pixels under the FWHM is 

$$\begin{equation}\mbox{N}_{\mbox{px}} = \displaystyle \frac{1.028\lambda F}{d}\end{equation}$$

which is nearly equivalent to $Q$. For a quick back of the envelope check, it is usually sufficient to use 

$$\begin{equation}\mbox{N}_{\mbox{px}} = Q\end{equation}$$

