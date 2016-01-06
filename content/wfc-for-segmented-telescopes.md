Title: Optimized Wavefront Control for Segmented Mirror Telescopes
Date: 2015-06-24
Modified: 2015-06-24
Category: control
Slug: wfc-for-segmented-telescopes
Status: draft

Consider a generalized segmented mirror telescope consisting of an n-segment primary mirror (PM) and a secondary mirror (SM). Each optical element may be actuated in six degrees of freedom (DOF) expressed in each mirror segment's coordinate frame: $x$, $y$, and $z$ translations and $\theta_x$, $\theta_y$, and $\theta_z$ rotations  (with $\theta_x$ and $\theta_y$ representing segment tip and tilt and $z$ representing segment piston).

An arbitrary alignment of the PM and SM results in overall system wavefront error (WFE); deviation of the wavefront at the image plane from its nominal value. Phase retrieval algorithms provide an approach to estimating WFE, which is in turn controlled through wavefront control (WFC) operations.

WFE is computed as follows

$$\mathbf{w} = \frac{dw}{dx} \mathbf{x}$$
where:

$\mathbf{w}$  = an $n_{\text{rays}} \times 1$ vector of optical path differences (OPD) of the spatially sampled wavefront.

$n_{\text{rays}}$  = the number of rays per wavefront.

$\displaystyle \frac{dw}{dx}$  = an $n_\text{rays} \times n_\text{states}$ linear sensitivity matrix relating changes in segment pose to resulting changes in OPD.

$\mathbf{x}$ = an $n_\text{states} \times 1$ vector of segment pose states.

Wavefront control is achieved through driving a set of rigid bodies (RB) mounted to each segment. Because the actuators take control commands in terms of their own length, we must derive an expression for the WFE in terms of RB actuator lengths. WFE is given as

$$\mathbf{w} = G\mathbf{u} =  \frac{dw}{dx}\frac{dx}{du} \mathbf{u}$$
where:

$\displaystyle\frac{dx}{du}$ = an $n_\text{states} \times n_\text{rb}$ linear sensitivity matrix relating changes in RB length to changes in segment pose.

$\mathbf{u}$ = an $n_\text{rb} \times 1$ vector of RB lengths.

### Unconstrained Least Squares WFC
For an arbitrary system with initial wavefront $\mathbf{w}_0$, we wish to find a command $\mathbf{u}$ which minimizes the resulting wavefront $\mathbf{w}$ in a least-squares sense. That is,

$$\min_\mathbf{u} \hspace{0.2em} \lvert\lvert \mathbf{w}\rvert\rvert_2^2$$ 

where: 

$$\mathbf{w} = G\mathbf{u} + \mathbf{w_0}$$

We solve for $\mathbf{u}$ by

$$\mathbf{u}_\text{ls} = (G^TG)^{-1}G^T\mathbf{w}_0 = G^\dagger \mathbf{w}_0$$

where $\dagger$ denotes the Moore-Penrose pseudoinverse. A solution for $\mathbf{u}_\text{ls}$ and the resulting post-control OPD is easily obtained from the following MATLAB code:

    :::matlab
    G = dwdx * dxdu;
    u = pinv(G) * w0;
    opd_controlled = G * u + w0;

While $\mathbf{u}_\text{ls}$ is indeed a least squares solution which minimizes $\mathbf{w}$, values of $\mathbf{u}$ are unconstrained and may be beyond the actuation limit of the rigid body actuators.


### Constrained Nonlinear Least Squares WFC
Again given an arbitraty system with initial wavefront $\mathbf{w}_0$:

$$\mathbf{w} = G\mathbf{u} + \mathbf{w}_0$$

We wish to find a command $\mathbf{u}$ which minimizes the wavefront $\mathbf{w}$ subject to actuation limits $u_\text{lb} \leq \mathbf{u} \leq u_\text{ub}$. MATLAB's `lsqnonlin` easily solves nonlinear least squares problems of the form

$$\min_\mathbf{x} \hspace{0.2em} \lvert\lvert f(x)\rvert\rvert_2^2$$ 

The following MATLAB code will determine the command vector $\mathbf{u}$ in a constrained-sense which minimizes $\mathbf{w}$:

    :::matlab
    G = dwdx * dxdu;

    fun = @(u) G * u + w0;              % minimization function
    x0 = zeros(n_rb, 1); 				% initial RB state estimate 
    lb = lower_bound * ones(n_rb, 1);   % lower bound on rb states
    ub = upper_bound * ones(n_rb, 1);   % upper bound on rb states

    u = lsqnonlin(fun, x0, lb, ub);
    opd_controlled = G * u + w0;

While `lsqnonlin` will converge on a command vector $\mathbf{u}$ which minimizes $\mathbf{w}$ within the boundary conditions, it is somewhat slow and often delivers a solution with several commands at or near their limits. In practice, this is a less than desirable situation. One approach to resolving this issue is to tighten the bounds on RB states. This is an acceptable solution when only small RB perturbations are required to minimize $\mathbf{w}$, but fails when actuators require larger strokes.

### Constrained Quadratic WFC
Again we have

$$\mathbf{w} = G\mathbf{u} + \mathbf{w}_0$$

We wish to find a command $\mathbf{u}$ which minimizes the wavefront $\mathbf{w}$ subject to actuation limits $u_\text{lb} \leq \mathbf{u} \leq u_\text{ub}$:

$$\min_\mathbf{u} \hspace{0.2em} \lvert\lvert \mathbf{w}\rvert\rvert_2^2 = \min_\mathbf{u} \mathbf{w}^T\mathbf{w}$$ 

Substituting in the original equation for $\mathbf{w}$,

\begin{align*}
\mathbf{w}^T\mathbf{w} &= (G\mathbf{u}+\mathbf{w}_0)^T(G\mathbf{u}+\mathbf{w}_0)\\
&= (\mathbf{u}^TG^T+{\mathbf{w}_0}^T)(G\mathbf{u}+\mathbf{w}_0)\\
&= \mathbf{u}^TG^T G\mathbf{u}+{\mathbf{w}_0}^T\mathbf{w}_0 + 2\mathbf{u^T}G^T\mathbf{w}_0
\end{align*}

The minimization problem is now

$$\min_\mathbf{u} \mathbf{u}^TG^T G\mathbf{u}+{\mathbf{w}_0}^T\mathbf{w}_0 + 2\mathbf{u^T}G^T\mathbf{w}_0$$

We can eliminate the middle term because it does not depend on $\mathbf{u}$, leaving us with 

$$\min_\mathbf{u} \mathbf{u}^TG^T G\mathbf{u} + 2\mathbf{u^T}G^T\mathbf{w}_0$$

MATLAB's `quadprog` finds a minimum for a problem specified by 

$$\min_\mathbf{x} \frac{1}{2}\mathbf{x}^T H \mathbf{x} + \mathbf{f}^T\mathbf{x}$$

After rewriting our objective function as

$$\min_\mathbf{u} \frac{1}{2}\mathbf{u}^TG^T G\mathbf{u} + \mathbf{u^T}G^T\mathbf{w}_0$$

we easily see that by setting $G^T G = H$ and $G^T \mathbf{w}_0 = \mathbf{f}^T \rightarrow \mathbf{f} = {\mathbf{w}_0}^T G$, we are able to use `quadprog` to compute $\mathbf{u}$. The following MATLAB code will determine  $\mathbf{u}$ in a constrained-sense which minimizes $\mathbf{w}$ using `quadprog`:

    :::matlab
    G = dwdx * dxdu;
    H = G' * G;
    f = w0' * G;

    x0 = zeros(n_rb, 1); 				% initial RB state estimate 
    lb = lower_bound * ones(n_rb, 1);   % lower bound on rb states
    ub = upper_bound * ones(n_rb, 1);   % upper bound on rb states
    opts = optimset('algorithm', 'interior-point-convex');

    u = quadprog(H,f,[],[],[],[],lb,ub,x0,opts);
    opd_controlled = G * u + w0;

### Multifield Constrained Quadratic WFC
Up to this point, we have generated commands which minimize the wavefront over one field point (commonly the center field point). Depending on the configuration of the optical system, this may be a sufficient control approach. In cases where it is not, we now extend the constrained quadratic control approach derived above to find a command $\mathbf{u}$ which minimizes a vector of stacked wavefronts $\mathbf{W}$
