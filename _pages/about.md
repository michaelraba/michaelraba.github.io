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

Overview of Msc Research: Effect of Rotation on a pipe's moderately turbulent flow using Reduced Order Modeling
======

<figure>
  <img src="/images/pipeT2.png" alt="Alt text">
  <figcaption>
cross section view of a single time instance of a flow of reynolds number $Re=11,700$
</figcaption>
</figure>

* Examine the flow's most energetic content *using Fourier-PCA analysis*, average in time, the azimuthal ($\theta$) direction $\in$ spectral domain.

This decomposition is useful to tease out the periodic nature of turbulence: despite the quasi-random nature of turbulence, after the above procedure, and averaging along the cross-section direction, we see there is a surprising structure to this chaos:

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

Procedure
======


1. take $f f t$ in streamwise $x$ direction $\leadsto$ wavenumber $k$
2. form complex-conjugate multiplication
3. form fft with azimuthal separation $\leadsto$ wavenumber $m$

\begin{align}
S_{i, j}\left(r, r^{\prime} ; m ; f\right)=\frac{1}{2 \pi} \sum_{\mathrm{m}=0}^N \tilde{S}_{i, j}\left(r, r^r ; \Delta \theta ; f\right) e^{-i m \Delta \theta} \mathrm{d}(\Delta \theta) 
\end{align} 

where

\begin{align}
\tilde{S}_{i, j}(r, r ; \Delta \theta ; f)=\frac{\left\langle\hat{u}_i(r, \theta, f) \hat{u}_j^*\left(r^{\prime}, \theta+\Delta \theta, f\right)\right\rangle}{T}
\end{align} 

which is more easily expressed as,

\begin{align}
\mathrm{S}\left(k ; m ; r, r^r\right)=\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau \mathrm{u}(k ; m ; r, t) \mathrm{u}^*\left(k ; m ; r^{\prime}, t\right) \mathrm{d} t
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
auto modulePath = "/home/miraba2/.totalview/lib_cache/cascadeb002/codes/sutekina/"; // /* hardcoded search path for module */
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

When passing C objects to Fortran, issues with memory alignment can arise due to differences in the memory layout and alignment requirements between the two languages. Memory alignment refers to the placement of data in memory at specific boundaries, often dictated by the size and type of the data, for example because of all of the below reasons:

* Data Type Size: Fortran typically has stricter alignment requirements compared to C. For example, in Fortran, 8-byte (64-bit) data types like real(c_double) often need to be aligned on an 8-byte boundary. If a C object contains such data types and the memory layout does not meet the alignment requirements of Fortran, misalignment issues can occur.

* Compiler and Platform Differences: Different compilers and platforms may have varying alignment requirements and memory layouts. If the C and Fortran code is compiled using different compilers or on different platforms, it can lead to inconsistencies in memory alignment.

* Structure Padding: C compilers may insert padding bytes between structure members for efficiency or alignment purposes. However, Fortran may not handle this padding correctly when accessing the structure, resulting in misalignment issues.

Memory alignment issues can occur when passing C objects to various other languages, not just specific ones. Here are a few examples of potential misalignment problems:

    C to C++: Although C++ is largely compatible with C, misalignment can still happen when passing C objects to C++ code due to differences in name mangling, inheritance, or virtual function tables. Additionally, C++ may introduce additional padding or alignment requirements, especially when dealing with classes, inheritance, or virtual functions.

    C to Rust: When passing C objects to Rust, memory alignment issues can arise. Rust has its own memory management and alignment rules, and it may require specific annotations or attributes to ensure proper alignment when interacting with C code.

    C to Python: Python, being a dynamically-typed language, often relies on C extensions for performance-critical operations. When passing C objects to Python, one need to ensure proper alignment to avoid memory access errors or data corruption.


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
<li> Next, the FFT-POD data is passed to matlab from memory. I omit showing this step for now. We can use either 1) matlab code which reads the above data via IO 2) converted matlab to C++ code.</li>

<li>  We want to take fourier transforms of $theta$ and streamwise direction $z$ (along the pipe), for all time $t$, and cross sections $x$. The proper data structure for this are nested structs. This data should be processed in parallel using OpenMP. </li>


Citations 
======
 1. Hellström LHO, Smits AJ.
2017 Structure identification in pipe flow using
proper orthogonal decomposition. Phil. Trans.
R. Soc. A 375: 20160086
