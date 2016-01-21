Title: Wavefront Control Part 1: Theory 
Date: 2016-01-13
Category: control
Tags: wfsc
Summary: This page presents a generalized wavefront control architecture for a segmented mirror telescope (for example, [Keck](https://en.wikipedia.org/wiki/W._M._Keck_Observatory) or [JWST](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)) with a [metrology](https://en.wikipedia.org/wiki/Metrology) system to measure segment state. This is the first in a two-part document covering theory. A follow-up document will present a MATLAB implementation of this theory.
Slug: wavefront-control-theory
Authors: AK

This page presents a generalized wavefront control architecture for a segmented mirror telescope (for example, [Keck](https://en.wikipedia.org/wiki/W._M._Keck_Observatory) or [JWST](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)) with a [metrology](https://en.wikipedia.org/wiki/Metrology) system to measure segment state. We assume the primary mirror segments and secondary mirror are controllable via a set of Rigid-Body Actuators (RBAs). We assume each segment and the SM have 6 RBAs allowing for full 6DOF control. Although it is not considered here, additional figure control may be available via deformable primary mirror segments.  

###LTI System Model

![Wavefront Control Architecture Block Diagram]({filename}/img/wavefront-control-theory-01.png)

**Figure 1** Wavefront Control Architecture

We can describe the system represented in the figure with an LTI system where

$$x(k+1) = \mathbf{A}x(t) + \mathbf{B}u(t) + w(k)\\
l(k) = \mathbf{C}x(t) + v(k)$$

The state (pose) vector for the $n^{th}$ optic is

$$x_n = \left[ \begin{array}{c}
R_{x,n}\\
R_{y,n}\\
R_{z,n}\\
T_{x,n}\\
T_{y,n}\\
T_{z,n}\end{array}\right]$$

and

$$x = \left[ \begin{array}{c}
x_1\\
\vdots\\
x_n\end{array}\right]$$
for all optics.

The control vector $u$ contains RBA commands and the output (measurement) vector $l$ contains metrology measurements.

The state transition matrix $\textbf{A} = \textbf{I}$, the input matrix $\mathbf{B} = \frac{dx}{du}$ maps RBA commands to segment pose, and the output matrix $\mathbf{C} = \frac{dl}{dx}$ maps segment pose to metrology measurements.

Process noise is captured by $w$ and measurement noise by $v$.

###State Estimator
The state estimator processes the metrology measurements to estimate the optical pose stste $\hat{x}$. Several options exist for implementing the state estimator:

####Least Squares Estimator
In the simplest case, a state estimate is obtained via least squares with

$$\hat{x}(k) = \displaystyle \left(\frac{dl}{dx}\right)^\dagger l(k) = \mathbf{K}l(k)$$

where $\dagger$ denotes the [Moore-Penrose pseudoinverse](https://en.wikipedia.org/wiki/Moore–Penrose_pseudoinverse).

####Weighted Least Squares Estimator

####Kalman Filter



For a MATLAB implementation of this architecture, see [Part 2]().

