Title: Nyquist Sampling and FPAs
Date: 
Tags: optics
Status: draft


## A note about critical sampling



 

### Nyquist
As it turns out, there seem to be several different thoughts on what constitutes critical sampling (Nyquist sampling criteria). The two prevailing thoughts are 

### Q
Q is a measure of the ratio between the fundamental resolution limits of the optics and the detector sampling. Quantitatively, it is given by:

$$Q = \displaystyle\frac{\lambda F}{d}$$

where $d$ is pixel size. Imaging performance falls in to three categories according to Q:

|   Q   | Resolution | Image appearance | Airy vs. pixel size |
|-------|------------|------------------|---------------------|
| Q<2 | Detector limited | Undersampled - images appear pixelated with ailiasing artifacts | Airy disk much smaller than pixel |
| Q=2 | Nyquist      | Critically sampled | Airy disk is 2x larger than pixel | 
| Q>2 | Optics limited | Oversampled - images may appear blurry | Airy disk much larger than pixel |

For Nyquist sampling there should be two pixels under an Airy disk (to the first minima). From (2) we calculate the pixel size to satisfy the Nyquist sampling criteria as:

$$d = 1.22\lambda F$$


