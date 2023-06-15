---
permalink: /
title: "About Michael Raba, MSc Candidate in Mechanical Engineering, University of Kentucky Pigman College of Engineering"
excerpt: "About Michael Raba, MSc Candidate in Mechanical Engineering, University of Kentucky Pigman College of Engineering"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a student in Mechanical Engineering with:
* Expertise in partial differential equations in both numerics and functional analytic viewpoints,
* Statistical approaches to fluid mechanics and large datasets <i>with an</i>
* Emphasis on scientific, MPI- and OpenMP-based parallel computing.

 <!-- Currently seeking a research grant-funded PhD position; See my Msc thesis <b>here (coming soon)</b> -->

Overview of MSc Research: Effect of Rotation on a pipe's moderately turbulent flow using Reduced Order Modeling
======

<figure>
  <img src="/images/pipeT2.png" alt="Alt text">
  <figcaption>
cross section view of a single time instance of a flow of reynolds number $Re=11,700$
</figcaption>
</figure>

* We would like to uncover a turbulent flow in a wall-bounded geometry (a pipe). Turbulent flows are highly stochastic, seemingly random. An engineering design goal could be flow relaminarization: it should be less chaotic. What is one way to achieve this?

Examine the flow's most energetic content *using Fourier-PCA analysis*: we can see there is an underlying regularity, so this chaos is really quasi-determinanistic! By working in the spectral domain, and looking at the first few PCA modes, we can represent most salient in a simplified way over time. This is almost magic.

A first hurdle to overcome is algorithm design, how can we engineer an effective implementation using parallel MPI, OpenMP, and vectorization, and data structures -- we need to thoughtfully lay out how to analyse large sets of data. 50 TB of direct numerical simulation data, which is multidimensional, and will be decomposed further in multiple Fourier directions, then PCA-decomposed, then averaged in different directions, involves good memory managmenent, careful parallelization, cacheing, and good algorithm design.


Next, we want to answer an engineering design question for our stakeholders: <i>could doing something as simple as rotating the pipe at a slow rate of rotation achieve our relaminarization goal?</i> When we rotate, do there emerge any coherent structures in the flow? How does the PCA modes of vectorial component related? If this question is answered, this can change how aerospace firms deal with say engine design such as rotating detonation engine. Maybe, using this rotation, it is possible to shorten a jet engine geometry, which is weight- and space saving. So it's an important question.



<figure>
  <img src="/images/m5.gif" alt="Alt text">
  <figcaption> <b>Structure in Randomness:</b> Most Energetic part of a <b>homogeneous wall-bounded turbulent flow</b> in a pipe. The 5th Azimuthal mode, $\langle\Phi^{(n=1,N=3.0,Re=5,300)}_x(r;\theta;m=5)\rangle_x$ is shown, where $n$ is the POD mode, $N=3.0$ is the swirl number, and $Re=5,300$ is the Reynolds number of a moderately turbulent flow. 
 
* Such POD decompositions form a 'cartoon' version of an otherwise complex turbulent flow, which we can engineer and also better control.</figcaption>
</figure>



<figure>
  <img src="/images/rotateN3.gif" alt="Alt text">
  <figcaption>
  A single cross section of a moderately turbulent flow $Re=11,700$ of the rotating pipe for rotation number $N=3.0$. The shear stress of the pipe's wall induces <i>relaminarization</i> which can be useful for flow control in turbomachinary
</figcaption>
</figure>



<figure>
  <img src="/images/eeset-1:1.gif" alt="Alt text">
  <figcaption> Coherent structure with iso-surface $\text{isovalue} = \mu \pm \sigma = 0.1$
</figcaption>
</figure>

* The most energetic content forms coherent structures, as above. They are hairpin-like structures even in rotation.

This research considers moderate turbulent numbers (5,300 and 11,700) using DNS. This method provides a highly accurate and detailed description of the fluid flow, including all scales of motion, from the smallest (Kolmogorov scale) to the largest (integral scale). However, DNS requires a significant computational cost, as the number of grid points needed scales with the Reynolds number to the power of 9/4, according to Kolmogorov's theory of turbulence. For a flow with a Reynolds number on the order of millions or tens of millions, like the one inside an engine nacelle, performing DNS would indeed be incredibly computationally intensive, so this study is more fundamental.

<figure>
  <img src="/images/place2.png" alt="Alt text">
  <figcaption> Showing the effects of rotation.
</figcaption>
</figure>

<figure>
  <img src="/images/place3.png" alt="Alt text">
</figure>

<figure>
  <img src="/images/place4.png" alt="Alt text">
  <figcaption> Showing two radial locations for each azimuthal mode where the POD modes 1 & 2 play a role in adding energy to $-\bar{uv}$
</figcaption>
</figure>

* We can reduce the magnitude of the Pipe's TKE (Turbulent Kinetic Energy) via rotation,and the extent away from the Wall the energy is most dominant. The TKE is less and the resulting Reynolds number $Re_\tau$ has been reduced. <b>Hence the flow is relaminarized</b>


Applications and Extension
======
* This Analysis finds use in flow control, such as rotating machinery
* Data was generated for Reynolds number $Re = \{5,300 , 11,700 \}$ for Rotation numbers $N = 0, 0.5, 1.0 , 2.0 , 3.0$
 * Work can be further extended by higher Reynolds numbers (eg $Re=50,000$), and using ML to interpolate (eg $Re=25,000$)
* Knowledge Domain :  Wall-bounded Turbulent Flows, Signal processing, Integral equations, Parallel Algorithm Design


Simulation Type: Spectral Element Method
======

Using spectral element solver NEK5000, the <i>direct numerical simulation</i> data is obtained using millions of compute hours. It must be also verified. Is the simuation converged, are boundary conditions correctly implemented and describe our goal? Is the mesh fine enough to capture the essential flow features, especially near the boundary. If these boundary conditions are not specified correctly, it can lead to physically unrealistic results. For example, an incorrectly specified outflow condition might lead to backflow at the outlet, which can cause numerical instabilities. By using benchmark studies, such as are known for a non-rotating pipe, we can become confident our simulation is correct -- gradually introducing the new rotation feature, examining the flow statistics under rotation.

Double Fourier-PCA Procedure
======


1. take $f f t$ in streamwise $x$ direction $\leadsto$ wavenumber $k$
2. form complex-conjugate multiplication
3. form fft with azimuthal separation $\leadsto$ wavenumber $m$

\begin{align}
S_{i, j}\left(r, r^{\prime} ; m ; k\right)=\frac{1}{2 \pi} \sum_{\mathrm{m}=0}^N \tilde{S}_{i, j}\left(r, r^{\prime}; \Delta \theta ; k\right) e^{-i m \Delta \theta} \mathrm{d}(\Delta \theta) 
\end{align} 

where

\begin{align}
\tilde{S}_{i, j}(r, r ; \Delta \theta ; k)=\frac{\left\langle\hat{u}_i(r, \theta, k) \hat{u}_j^*\left(r^{\prime}, \theta+\Delta \theta, k\right)\right\rangle}{x}
\end{align} 

which is more easily expressed as,

\begin{align}
\mathrm{S}\left(k ; m ; r, r^{\prime}\right)=\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau \mathrm{u}(k ; m ; r, t) \mathrm{u}^*\left(k ; m ; r^{\prime}, t\right) \mathrm{d} t
\end{align} 

using symmetry to elimate imaginary components of the complex signal via 

\begin{align}
\Phi_x^{(n)}(k ; m ; r)=\Phi_x^{(n)}(k ;-m ; r)=\Phi_x^{(n)^*}(-k ; m ; r)
\end{align} 

and normalizing via the inner product,

\begin{align}
\begin{aligned}
\left\langle\phi_j, \phi_k\right\rangle & =\int_A \phi_j \cdot \phi_k d A=\int_{[0,2 \pi]} \int_{[0, R]} \phi\left(r_j\right) \cdot \phi\left(r_k\right)^{\dagger} r_i d r d \theta \\
& =2 \pi \sum_{[0, R]} \phi\left(r_j\right) \cdot \phi\left(r_k\right)^{\dagger} r_i\left(\frac{r_i-r_{i-1}}{n}\right)
\end{aligned}
\end{align} 

we can recover the images presented on this page.

Requirements and Data Structures
======

1. Requirement: Model a turbulent flow through a pipe using high-fidelity DNS simulation. 
2. Large Data and its organization: 40 TB of data in .hdf5 format using compression filter (lzf)  
3. The turbulent data must be decompressed from a propriatary format and kept organized 
4. Once decompressed, the data must be interpolated along different spatial extents.
5. IO must be avoided in steps 2-4, so python-c++ and c++-fortran data must be passed in memory. This must be carefully done (memory alignment requirement) so the data is accurately represented after the pass.
6. This data represents vector components $(u_r,u_\theta,u_z,p)$ expressed in  
the pipe's cylindrical coordinates, along with pressure $p$. 
7. Requirement: Using a technique called 'Proper Orthogonal Decomposition', capture the most energetic part of the signal. This is what allows us to form the pictures above, on this page. The POD is analogous to the fourier transform -- the difference is the basis is boutique, based on the dataset, rather than sines and cosines. 
8. The data may be represented by Fourier series in the azimuthal ($\theta$) direction, and in the $z$-direction, since the simulation's boundary conditions are periodic.
9. After decompositng, that is a lot of data, which must be kept in order. 
An inefficient way to store this data is in a multi-dimensional array. Since the data is inhomogeneous -- each dimension, eg $x$, $t$, $\theta$ and its fourier-modes $m$, the streamwise direction and its fourier modes $k$, are of different sizes, the more efficient data structure are nested structures. This allows for better memory management.

{% highlight cpp %}
Py_Initialize();
auto modulePath = "/path/to/python/code"; // /* hardcoded search path for module */
PyObject* sysPath = PySys_GetObject("path");
assert(PyArray_API);
cout << "2a\n";  PyObject* nekMod = PyImport_ImportModule("d");
PyObject* arg = Py_BuildValue("(i)", snapshot); // this created tuple is used for the function ff, which takes an arg (time).
PyObject* nekFf = PyObject_GetAttrString(nekMod, "ff");
PyObject* resultFf = PyObject_CallObject(nekFf, arg);
cout<<"*mm1:\n";PyArrayObject* arrZ = reinterpret_cast<PyArrayObject*>(resultFf);
int ndim = arrZ->nd;
npy_intp* shape = arrZ->dimensions;
npy_intp* shape2 = PyArray_DIMS(arrZ); // same thing as shape; both return correct vals.
std::cout << "Dimensions: "; // print out dimension with for-loop
for (int i = 0; i < ndim; i++) {
  std::cout << shape[i] << " ";
  std::cout << shape2[i] << " ";
}
const int ncs=150;
const int nPts=58032;
struct varStr fullVars;
fullVars.U = new double*[ncs];
fullVars.V = new double*[ncs];
fullVars.W = new double*[ncs];
fullVars.P = new double*[ncs];
for (int i = 0; i < ncs; i++) { // i =cs
  fullVars.U[i] = new double[nPts];
  fullVars.V[i] = new double[nPts];
  fullVars.W[i] = new double[nPts];
  fullVars.P[i] = new double[nPts];
}
{% endhighlight %}


<ol start="10">

<li> We pass this data to legacy Fortran code, which is fortran 2018 standard.
The analoge for C-structs in fortran are called 'derived types'. </li>

<p>When passing C objects to Fortran, issues with memory alignment can arise due to differences in the memory layout and alignment requirements between the two languages. Memory alignment refers to the placement of data in memory at specific boundaries, often dictated by the size and type of the data, for example because of all of the below reasons:</p>

<li> Data Type Size: Fortran typically has stricter alignment requirements compared to C. For example, in Fortran, 8-byte (64-bit) data types like real(c_double) often need to be aligned on an 8-byte boundary. If a C object contains such data types and the memory layout does not meet the alignment requirements of Fortran, misalignment issues can occur. </li>

<li> Compiler and Platform Differences: Different compilers and platforms may have varying alignment requirements and memory layouts. If the C and Fortran code is compiled using different compilers or on different platforms, it can lead to inconsistencies in memory alignment.</li>

<li> Structure Padding: C compilers may insert padding bytes between structure members for efficiency or alignment purposes. However, Fortran may not handle this padding correctly when accessing the structure, resulting in misalignment issues.</li>

<li> Memory alignment issues can occur when passing C objects to various other languages, not just specific ones. Here are a few examples of potential misalignment problems:</li>

<li> C to C++: Although C++ is largely compatible with C, misalignment can still happen when passing C objects to C++ code due to differences in name mangling, inheritance, or virtual function tables. Additionally, C++ may introduce additional padding or alignment requirements, especially when dealing with classes, inheritance, or virtual functions.</li>

<li> C to Python: Python, being a dynamically-typed language, often relies on C extensions for performance-critical operations. When passing C objects to Python, one need to ensure proper alignment to avoid memory access errors or data corruption.</li>
</ol>

{% highlight fortran %}
! read c++-structures into array
! for function 'interpolate-pipe'
type(varStr) :: fullVars
type(c_ptr), pointer :: U_ptr, V_ptr, W_ptr, P_ptr
real(c_double), pointer :: U(:,:), V(:,:), W(:,:), P(:,:)
integer :: start_time(8), end_time(8), elapsed_time, wait_time
call c_f_pointer(fullVars%U, U_ptr) ! nb all 8 calls are req'd vvvvvvvvvvvv
call c_f_pointer(fullVars%V, V_ptr)
call c_f_pointer(fullVars%W, W_ptr)
call c_f_pointer(fullVars%P, P_ptr)
call c_f_pointer(U_ptr, U, [nPts,ncs])
call c_f_pointer(V_ptr, V, [nPts,ncs])
call c_f_pointer(W_ptr, W, [nPts,ncs])
call c_f_pointer(P_ptr, P, [nPts,ncs]) ! nb all 8 calls are req'd ^^^^^^^^^
{% endhighlight %}

<ol start="11">
<li> Next, the FFT-POD data is passed to matlab from memory. We can use either 1) matlab code which reads the above data via IO 2) converted matlab to C++ code.</li>



<figure>
  <img src="/images/dataTree.png" alt="Alt text">
  <figcaption> Organization of structs of structs of structs forms a data tree. 
   For example, <code>dataStructTimeData(t).azimuthDir(m).radialDir(r).zeeDir(z)</code> is organized to Fourier-transform streamwise since the child nodes are in z. The procedure can less optimally be organized as e.g., a 4-dimensional array.
</figcaption>
</figure>



<li>  We fourier transform in $\theta$ and streamwise direction $z$ (along the pipe), for all time $t$, and radial locations $r$. The DNS data is sufficiently resolved near the wall and after interpolating from a nonuniform grid, is also sufficient resolution in radial and streamwise direction, such that the 2d eigenmodes form clear patterns after averaging over 1000 timesteps and 100 streamwise locations. 

The proper data structure for this are nested structs. This procedure is embarassingly parallelizable, such that this procedure can be performed with 48 cores in around 30 minutes.</li>
</ol>
 
Two-dimensional Eigenmode Projections
======

<figure>
  <img src="/images/w3.jpg" alt="Alt text">
  <img src="/images/w4.jpg" alt="Alt text">
  <figcaption>
2rd order POD mode for rotation number $N=1$ and azimuthal mode $m=11$
</figcaption>
</figure>



<p>
<object data="/assets/2dmodes.pdf" type="application/pdf" width="100%" height="600px">
  <p>It appears you don't have a PDF plugin for this browser. No worries, you can <a href="/assets/2dmodes.pdf">click here to download the PDF file</a>.</p>
</object> </p>

Meshing and Interpolation 
======

<figure>
  <div style="display: flex; justify-content: space-around;">
    <div style="width: 65%;">
      <img src="/images/meshPre.png" alt="Alt text" style="width: 60%; display: block; margin: auto;">
      <figcaption style="text-align: center;">(a) Pre-interpolated nonuniform mesh (GLL Elements) with higher resolution near the pipe wall of the DNS model</figcaption>
    </div>
    <div style="width: 55%;">
      <img src="/images/meshPre2.png" alt="Alt text" style="width: 60%; display: block; margin: auto;">
      <figcaption style="text-align: center;">(b) Closeup of the 6 Gauss-Legendre-Lebesgue Elements</figcaption>
    </div>
  </div>
  <div style="width: 75%; margin-top: 20px; margin-left: auto; margin-right: auto;">
    <img src="/images/meshPost.png" alt="Alt text" style="width: 60%; display: block; margin: auto;">
    <figcaption style="text-align: center;">(c) Uniform Interpolated Mesh consisting of lines radiading outward of distance $r_i$ at angle $\theta_j$</figcaption>
  </div>
</figure>

 In the realm of spectral element solvers, GLL mesh is the "tipping point" in algorithmic efficiency. Three stand-out benefits are its spectral accuracy, efficient computation of differential operators, and its knack for capturing localized phenomena. Due to the nature of fluid dynamics, elements of turbulence near the pipe wall require finer meshes, akin to watching a basketball game courtside - a more intimate and detailed view.


Eigenproblem Setup
======

POD Method of Snapshots: form symmetric eigenvalue problem $\in \mathbb{C}$ 

\begin{align}
\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau \mathrm{S}\left(k ; m ; t, t^{\prime}\right) \alpha^{(n)}\left(k ; m ; t^{\prime}\right) d t^{\prime} \\
=\lambda^{(n)}(k ; m) \alpha^{(n)}(k ; m ; t) .
\end{align} 

Using Hilbert-Schmidt theory, can expand in terms of eigenfunctions, and the integral kernel is symmetric Hermitian. This is just 

\begin{align}
\int K(x, y) \varphi(y) d y=
\lambda \varphi(x) \quad \Leftrightarrow  \sum_j M_{i, j} v_j=\lambda v_i
\end{align} 

where $\mathbf{M}=\left[M_{i, j}\right]$ is a matrix, $\mathbf{v}$ is one of its eigenvectors, and $\lambda$ is the associated eigenvalue. Taking the continuum limit, i.e., replacing the discrete indices $i$ and $j$ with continuous variables $X$ and $y$, and gives a linear homogeneous Fredholm equation of the second type equation. Note that the kernel being Hermitian symmetric is what guarantees a unique solution to the integral equation.

Solve for $\Phi$

\begin{align}
\lim_{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau \mathbf{u}_{\mathrm{T}}(k ; m ; r, t) \alpha^{(n)^{\dagger}}(k ; m ; t) dt=\Phi_T^{(n)}(k ; m ; r) \lambda^{(n)}(k ; m)
\end{align} 

Classical Approach
======

Snapshot POD infamously has 'mode-mixing', that is, the savings of temporal cross-correlating comes at the cost of
slightly incorrect results. The classical approach, while slower, is more accurate, but has more computations. Further, in order to
not break Hilbert-Schmidt theory --- we are, after all, solving a discretized integral equation, which has a solution only under certain conditions --- we 
must decompose the $r$ weight as


\begin{align}
\overline{\boldsymbol{S}}\left(m ; r, r^{\prime}\right) & =\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau (r^{\prime})^{1/2} \boldsymbol{u}(m ; r, t) \boldsymbol{u}^*\left(m ; r^{\prime}, t\right) r^{1 / 2}\, dt 
\end{align} 




References
======

Raba, M. (2023). <i>Structure identification in Rotating Pipe Flow</i>. (master's thesis). University of Kentucky.
