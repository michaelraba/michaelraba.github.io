---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: space-between;
}
.cv-column {
  flex: 1 1 45%;
  min-width: 300px;
}
.cv-column h2 {
  margin-top: 0;
}
</style>

<div class="cv-container">
  <div class="cv-column">
    <h2>Work Experience</h2>
    <ul>
      <li><strong>Fall 2020–2023:</strong> Research Assistant
        <ul>
          <li>National Science Foundation</li>
          <li>Reduced Order Modeling of Moderate Reynolds Number Flows in a Rotating Pipe</li>
          <li>Supervisor: Prof. Christoph Brehm (UMD College Park)</li>
        </ul>
      </li>
      <li><strong>Spring 2023:</strong> Teaching Assistant
        <ul>
          <li>ANOVA, DOE; windtunnel, strain gage, beam deflection, LabView</li>
        </ul>
      </li>
      <li><strong>Fall 2020:</strong> TA for Thermodynamics II</li>
      <li><strong>Spring 2018:</strong> TA for Fluid Mechanics I</li>
      <li><strong>Summer 2018:</strong> Research Assistant
        <ul>
          <li>UK Dept. of Aerospace Engineering</li>
          <li>CFD air filter design with STAR-CCM+, Linux toolchain</li>
        </ul>
      </li>
    </ul>

    <h2>Education</h2>
    <ul>
      <li><strong>M.Sc Mechanical Engineering</strong>, Univ. of Kentucky, Spring 2025</li>
      <li><strong>B.A. Applied Mathematics</strong>, Univ. of Kentucky, Spring 2019</li>
    </ul>
  </div>

  <div class="cv-column">
    <h2>Skill 1 – Scientific Parallel Computing</h2>
    <ul>
      <li>MPI, OpenMP (C++11/14/17, Fortran2018, Julia, Python, Matlab)</li>
      <li>Standard C++: STL, resource management, concurrency, Boost, Eigen</li>
      <li>Interoperability: &lt;python, c++, fortran, julia&gt;</li>
      <li>Memory profiling: Vtune, Valgrind, gdb, totalview</li>
      <li>HDF5, SZIP/LZF for large data</li>
      <li>Git: branching/merging, CI/CD automation</li>
      <li>Linux optimization: CentOS, Arch, Ubuntu</li>
    </ul>

    <h2>Skills</h2>
    <ul>
      <li>Signal Processing (Fourier)</li>
      <li>Reduced Order Modeling</li>
      <li>Turbulence theory</li>
      <li>Matrix Methods</li>
      <li>Technical writing</li>
      <li>Ansys Workbench, STAR-CCM+</li>
    </ul>
  </div>
</div>
