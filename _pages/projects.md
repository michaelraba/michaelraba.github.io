---
layout: single
title: "Projects"
permalink: /projects/
excerpt: "Engineering projects by Michael Raba: controls, machine design, FEA, acoustics, material modeling and reduced-order modeling."
author_profile: true
redirect_from:
  - /talks/
  - /portfolio/
---

<script type="module" src="https://unpkg.com/@google/model-viewer@3.5.0/dist/model-viewer.min.js"></script>

Each project lists what the problem was, what I did, and the tools I used. Most include the full slide deck I presented;
the decks open in a new tab and use the arrow keys to move between slides.

<div class="proj-toc">
  <a href="#ball-on-beam">Ball-on-beam control</a>
  <a href="#shaft-design">Motor shaft design</a>
  <a href="#pod">MSc: pipe flow ROM</a>
  <a href="#muffler">Muffler acoustics</a>
  <a href="#anand">Solder viscoplasticity</a>
  <a href="#fea-optimization">FEA optimization</a>
  <a href="#software">Software tools</a>
</div>

<p class="section-label">Design and controls</p>

<div class="proj-detail" id="ball-on-beam">
  <div>
    <model-viewer src="{{ site.baseurl }}/assets/controlsProj/glb/full.glb"
                  alt="3D CAD model of the ball-on-beam rig"
                  camera-controls auto-rotate camera-orbit="35deg 65deg auto"
                  shadow-intensity="1" exposure="0.9">
      <img slot="poster" src="{{ site.baseurl }}/images/projects/ball-on-beam.png" alt="Rendering of the ball-on-beam rig" style="width:100%;height:100%;object-fit:contain;border:none;">
    </model-viewer>
    <div class="media-note">Drag to rotate, scroll to zoom.</div>
  </div>
  <div>
    <h2>Ball-on-Beam Closed-Loop Control</h2>
    <p class="proj-meta">ME/AER 440 team project, University of Kentucky, Fall 2026 (in progress)</p>
    <p>A servo tilts a beam so that a ball rolls to, and holds, a commanded position. The ball's position is read by a
       time-of-flight distance sensor and fed back to the controller.</p>
    <ul>
      <li>Derived the ball-on-beam plant dynamics and built the system model in Simulink for controller design.</li>
      <li>Team design. Mechanism: Hitec HS-5645MG servo driving the beam through a rod-end linkage at about 4:1, with a preload spring to take out backlash.</li>
      <li>Center pivot on an M5 shoulder bolt with two MR106ZZ bearings, set by a sleeve and shims and held with a nylon-lock nut.</li>
      <li>Beam: two 4 mm rails, 300 mm long and 16 mm apart, with end stops. Sensor: VL53L1X mounted so the ball never comes closer than its 40 mm minimum range.</li>
      <li>Controller runs on an Arduino.</li>
    </ul>
    <div class="tags"><span>Controls</span><span>Simulink</span><span>Arduino</span><span>Mechanism design</span><span>CAD</span></div>
    <div class="proj-links">
      <a class="btn-link" href="{{ site.baseurl }}/assets/controlsProj/partA-3.html" target="_blank" rel="noopener">3D assembly walkthrough (each subassembly)</a>
    </div>
  </div>
</div>

<div class="proj-detail" id="shaft-design">
  <div>
    <img src="{{ site.baseurl }}/images/projects/bolt-fea.png" alt="Finite element model of a threaded joint">
    <div class="media-note">Shown: related FEA work on a threaded joint (ME 514). Shaft design report to be added when complete.</div>
  </div>
  <div>
    <h2>Shaft and Drivetrain Design for a 40 HP Motor</h2>
    <p class="proj-meta">ME 344 Machine Design project, University of Kentucky, Fall 2026 (in progress)</p>
    <p>Designing the shaft and drivetrain components driven by a 40 HP, 1750 RPM electric motor that lifts a load, sized for both static strength and fatigue.</p>
    <ul>
      <li>Free-body diagrams and symbolic equations for each component, valid for every design iteration.</li>
      <li>Static and fatigue safety factors following Shigley's method (endurance limit modifiers, stress concentrations, fatigue failure criteria).</li>
      <li>Design alternatives iterated in Excel, with final geometry modeled in CAD and documented in a design report.</li>
    </ul>
    <div class="tags"><span>Machine design</span><span>Fatigue</span><span>Shigley</span><span>Excel</span><span>CAD</span></div>
  </div>
</div>

<p class="section-label">Simulation and analysis</p>

<div class="proj-detail" id="pod">
  <div>
    <img src="{{ site.baseurl }}/images/projects/pod-modes.png" alt="Reconstructed versus original turbulent velocity field in a pipe cross-section">
    <div class="media-note">A turbulent snapshot (right) rebuilt from a small number of POD modes (left).</div>
  </div>
  <div>
    <h2>MSc Project: Reduced-Order Modeling of Turbulent Rotating Pipe Flow</h2>
    <p class="proj-meta">MSc, University of Kentucky, 2020&ndash;2025; final presentation December 2025</p>
    <p>When a pipe spins about its own axis, turbulence in the flow can be suppressed and the flow partly relaminarizes,
       which matters for rotating heat exchangers and turbomachinery. I used Proper Orthogonal Decomposition (POD) to
       find which flow structures carry the energy and how they change with rotation.</p>
    <ul>
      <li>Wrote an object-oriented MATLAB framework that reads the simulation output, applies FFTs in the periodic directions and computes both classic and snapshot POD.</li>
      <li>Analyzed high-fidelity Nek5000 DNS data at Re = 5,300 for swirl rates from 0 to 3, reducing about 5 TB of data to a small set of energy-ranked modes.</li>
      <li>Showed how large-scale motions near the wall weaken as rotation increases, linking the mode energy distribution to relaminarization.</li>
      <li>Collaborated with PhD researchers at the University of Maryland and the University of Oxford; attended the AIAA Aviation Forum (2022).</li>
    </ul>
    <div class="tags"><span>MATLAB</span><span>Python</span><span>C++ / Fortran</span><span>Linux / HPC</span><span>Fluid mechanics</span></div>
    <div class="proj-links">
      <a class="btn-link" href="{{ site.baseurl }}/assets/msc/msc.html" target="_blank" rel="noopener">Final MSc presentation</a>
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/qme.html" target="_blank" rel="noopener">How the MATLAB code is organized</a>
    </div>
  </div>
</div>

<div class="proj-detail" id="muffler">
  <div>
    <img src="{{ site.baseurl }}/images/projects/muffler.png" alt="Multichamber muffler internal geometry">
  </div>
  <div>
    <h2>Multichamber Muffler Design</h2>
    <p class="proj-meta">Engineering Acoustics course design competition, University of Kentucky</p>
    <p>Design a muffler that gives the most insertion loss (noise reduction) across the frequency range, then compare the
       prediction with measurements from the built muffler.</p>
    <ul>
      <li>Designed the internals: multiple chambers, baffles, perforated tubes and a fiberglass absorber.</li>
      <li>Simulated transmission loss from 0 to 1000 Hz in ANSYS Workbench (Acoustics), modeling the air at 20&nbsp;&deg;C.</li>
      <li>Built an independent 1D transfer-matrix model in SIDLAB as a check on the 3D results.</li>
      <li>Compared simulated and measured insertion loss and published both model files so the results can be reproduced.</li>
    </ul>
    <div class="tags"><span>ANSYS Acoustics</span><span>SIDLAB</span><span>NVH</span><span>Test vs. simulation</span></div>
    <div class="proj-links">
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/510finalProj/510fp.html" target="_blank" rel="noopener">Presentation with 3D viewer</a>
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/510finalProj/files/Mark-I-MDF-clearned-data.wbpz">ANSYS project file</a>
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/510finalProj/files/Mark3Sid.zip">SIDLAB model</a>
    </div>
  </div>
</div>

<div class="proj-detail" id="anand">
  <div>
    <img src="{{ site.baseurl }}/images/projects/anand-solder.png" alt="Predicted stress versus inelastic strain for a solder alloy at several temperatures">
    <div class="media-note">Predicted stress&ndash;strain curves for 62Sn36Pb2Ag solder from &minus;55&nbsp;&deg;C to 125&nbsp;&deg;C.</div>
  </div>
  <div>
    <h2>Viscoplastic Modeling of Solder Joints (Anand Model)</h2>
    <p class="proj-meta">Plasticity course project, University of Kentucky</p>
    <p>Solder joints in electronics packages creep and fail under thermal cycling. Anand's unified viscoplastic model
       captures how solder stress depends on strain rate and temperature, and it is built into ANSYS for modeling these alloys.</p>
    <ul>
      <li>Implemented the Anand flow rule and deformation-resistance evolution in Python with a forward Euler time integrator.</li>
      <li>Reproduced published test data for solder at strain rates of 10<sup>&minus;2</sup> and 10<sup>&minus;4</sup> s<sup>&minus;1</sup>, then used the code to check the ANSYS nonlinear material model.</li>
      <li>Built an interactive Plotly figure for exploring stress&ndash;strain response across temperature.</li>
    </ul>
    <div class="tags"><span>Python / NumPy</span><span>ANSYS nonlinear materials</span><span>Electronics reliability</span></div>
    <div class="proj-links">
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/603talk/603fp.html" target="_blank" rel="noopener">Presentation</a>
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/603talk/wang_stress_strain.html" target="_blank" rel="noopener">Interactive stress&ndash;strain plot (7 MB)</a>
    </div>
  </div>
</div>

<div class="proj-detail" id="fea-optimization">
  <div>
    <img src="{{ site.baseurl }}/images/projects/microgripper.png" alt="Deformed compliant microgripper arm in ANSYS">
  </div>
  <div>
    <h2>FEA Design Optimization in ANSYS Workbench</h2>
    <p class="proj-meta">ME 514 Machine Design using ANSYS Workbench, University of Kentucky, Fall 2024</p>
    <ul>
      <li><strong>Compliant microgripper:</strong> parameterized the arm geometry and used ANSYS's adaptive single-objective optimizer to maximize the gripper's motion amplification while keeping stress at or below 15 MPa.</li>
      <li><strong>Threaded joint:</strong> modeled a bolt and nut with frictional contact (&mu; = 0.2) using symmetry and a 2D model to cut solve time, and showed how load concentrates on the first few engaged threads.</li>
    </ul>
    <div class="tags"><span>ANSYS Workbench</span><span>Optimization</span><span>Contact</span><span>Meshing</span></div>
    <div class="proj-links">
      <a class="btn-link" href="{{ site.baseurl }}/assets/mikePres/smallPortfolio/smallPort.pdf" target="_blank" rel="noopener">Project poster (PDF)</a>
    </div>
  </div>
</div>

<p class="section-label">Software and automation</p>

<div class="proj-detail" id="software">
  <div>
    <h2>Software tools</h2>
    <p class="proj-meta">Built at UK HealthCare (2019&ndash;present) and earlier coursework</p>
  </div>
  <div>
    <ul>
      <li><strong>Hospital wayfinding app:</strong> a web app (Flask, Python, SQL) that gives visitors directions through the medical center.</li>
      <li><strong>Directory lookup tool:</strong> a desktop tool (AutoHotkey v2 with an HTML interface) that takes text copied from the electronic health record, fuzzy-matches it against the department phone directory and shows the closest matches, ranked, so calls get routed faster.</li>
      <li><strong>Earlier work:</strong> a 3D finite-difference time-domain solver (Yee scheme) for tracking a particle in a magnetized fluid flow (2019).</li>
    </ul>
    <div class="tags"><span>Python</span><span>Flask</span><span>SQL</span><span>AutoHotkey</span><span>Numerical methods</span></div>
  </div>
</div>
