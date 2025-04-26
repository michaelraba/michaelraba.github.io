#!/usr/bin/env python3.10
from manim import *
import numpy as np
class AnandSigmaVsEpsDot(Scene):
   def construct(self):
       # Axes setup
       axes1 = Axes(
           x_range=[0, 2e4, 4000],
           y_range=[0, 150, 30],
           x_length=6,
           y_length=5,
           axis_config={"include_numbers": True},
       ).to_edge(LEFT)
       x_label1 = axes1.get_x_axis_label(Tex(r"$\dot{\varepsilon}^p$"))
       y_label1 = axes1.get_y_axis_label(Tex(r"$\sigma$ (MPa)"))
       title1 = Text("$\sigma$ vs $\dot{\varepsilon}^p$", font_size=24).next_to(axes1, UP)
       self.play(
           Create(axes1),
           Write(x_label1),
           Write(y_label1),
           Write(title1),
       )
       # Constants from 60Sn40Pb
       A = 1.49e7  # s^-1
       Q_div_R = 10830  # K
       T = 298  # K
       j = 11
       s = 50  # Assume s ~ sigma steady state
       exp_factor = np.exp(-Q_div_R / T)
       # Tracker for m
       m_tracker = ValueTracker(0.1)
       # Define eps_dot values (x axis)
       eps_dot_vals = np.linspace(1e2, 2e4, 300)
       def get_color(m):
           return interpolate_color(ORANGE, BLUE, (m - 0.005) / (1.0 - 0.005))
       def get_sigma_curve():
           m = m_tracker.get_value()
           sigma_vals = []
           for eps_dot in eps_dot_vals:
               sinh_inv_arg = (eps_dot / (A * exp_factor)) ** m
               sigma = (np.arcsinh(sinh_inv_arg)) * s / j
               sigma_vals.append(sigma)
           return axes1.plot_line_graph(
               x_values=eps_dot_vals,
               y_values=sigma_vals,
               add_vertex_dots=False,
               line_color=get_color(m),
               stroke_width=4,
           )
       # Always redraw curve
       sigma_curve = always_redraw(get_sigma_curve)
       m_label = always_redraw(
           lambda: MathTex(f"m = {m_tracker.get_value():.3f}").scale(0.8).to_corner(UL)
       )
       self.add(sigma_curve, m_label)
       self.play(m_tracker.animate.set_value(1.0), run_time=8)
       self.wait()
