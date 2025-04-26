#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandStrainVsStress(ThreeDScene):
    def construct(self):
        # Constants
        A = 1.0
        Q = 1.0
        R = 1.0
        T = 1.0
        xi = 1.0
        s = 1.0
        # Axes (strain on x-axis, stress on y-axis)
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 0.5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)
        x_label = axes.get_x_axis_label(MathTex(r"\varepsilon^p"))
        y_label = axes.get_y_axis_label(MathTex(r"\sigma"))
        title = Text(
            "Stress vs. Plastic Strain ($\\sigma$ vs. $\\varepsilon^p$)", font_size=30
        ).to_edge(UP)
        self.play(Create(axes), Write(x_label), Write(y_label), Write(title))
        # ValueTracker for m
        m_tracker = ValueTracker(0.05)

        # Animated plot of strain vs. stress
        def get_graph():
            m = m_tracker.get_value()
            sigma_vals = np.linspace(0.01, 3, 300)
            dot_eps_p = A * np.exp(-Q / (R * T)) * np.sinh(xi * sigma_vals / s) ** m
            eps_p = np.cumsum(dot_eps_p) * (sigma_vals[1] - sigma_vals[0])
            return axes.plot_line_graph(
                x_values=eps_p,
                y_values=sigma_vals,
                add_vertex_dots=False,
                line_color=interpolate_color(RED, BLUE, m / 0.5),
                stroke_width=4,
            )

        graph = always_redraw(get_graph)
        # Display current m value
        m_display = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.8)
            .next_to(axes, UR)
        )
        self.add(graph, m_display)
        self.play(m_tracker.animate.set_value(0.5), run_time=6, rate_func=linear)
        self.wait()
