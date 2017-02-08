Title: Zernike Mode Removal 
Date: 2016-02-17
Category: 
Tags:
Summary: 
Slug: zernike-mode-removal
Authors: AK
Status: draft

The [Zernike polynomials](https://en.wikipedia.org/wiki/Zernike_polynomials) represent an orthogonal basis defined over the unit circle and an arbitrary wavefront over a circular pupil can be described as a linear combination of Zernike polynomials:

$$w(x,y) = \displaystyle \sum_{n = 1}^\infty z_n a_n(x,y)$$

We can exploit this fact to easily remove certain Zernike modes from a wavefront - most commonly the piston ($Z_1$) or piston, tip, and tilt ($Z_1:Z_3$) terms. 

Let's consider the case where we remove tip, tilt, and piston. To simplify the math and enable us to simultaneously remove multiple modes we reshape the wavefront and each Zernike mode matrix into a column vector. We now have 

$$w = \mathbf{Z}c + \displaystyle \sum_{n=4}^\infty z_n a_n \hspace{1em}\mbox{where}\hspace{0.25em} \mathbf{Z} = \left[\begin{array}{ccc}z_1&z_2&z_3\end{array}\right]$$
 
At this point we are only concerned with the piston, tip, and tilt components of the wavefront so we can ignore the higher-order terms represented by the sum in the above expression, leaving us with the following equation:

$$w = \mathbf{Z}c$$

We solve this system of linear equations by least squares:

$$c = \mathbf{Z}^\dagger w$$

The vector $c$ contains the contributions of piston, tip, and tilt contained in the wavefront $w$. These modes are easily removed by simply subtracting them out of the wavefront:

$$w_1 = w - Zc$$

This can be implemented in a few lines of MATLAB as follows:

    :::matlab
    w = w(:);
    Z = [z1(:) z2(:) z3(:)];  % piston, tip, and tilt Zernikes
    
    w_nottp = w - w*(Z\w);

In cases where we need to remove the same Zernike modes from a large number of different wavefronts, it is more efficient to multiply by a precomputed $G = Z^\dagger$ matrix than to use MATLAB's linear equation solver each time: 

    :::matlab
    w = w(:);
    Z = [z1(:) z2(:) z3(:)];
    G = pinv(Z);

    w_nottp = w - w*(G*w)

Because the Zernike polynomials are orthogonal, these two approaches give the same result.
