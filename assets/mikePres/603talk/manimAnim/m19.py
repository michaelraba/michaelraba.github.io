#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandSideBySideGraphs(Scene):
    def construct(self):
        # Constants
        A = 1.0
        Q = 1.0
        R = 1.0
        T = 1.0
        xi = 1.0
        s = 1.0
        # Tracker for m
        m_tracker = ValueTracker(0.05)
        # Axes for dot{ep} vs sigma (left)
        axes_left = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
        )
        # Axes for ep vs sigma (right)
        axes_right = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
        )
        # Combine and position
        axes_group = VGroup(axes_left, axes_right).arrange(RIGHT, buff=1).to_edge(DOWN)
        self.play(Create(axes_group))
        # Labels
        x_label_left = axes_left.get_x_axis_label(MathTex(r"\sigma"))
        y_label_left = axes_left.get_y_axis_label(MathTex(r"\dot{\varepsilon}^p"))
        x_label_right = axes_right.get_x_axis_label(MathTex(r"\varepsilon^p"))
        y_label_right = axes_right.get_y_axis_label(MathTex(r"\sigma"))
        self.play(
            Write(x_label_left),
            Write(y_label_left),
            Write(x_label_right),
            Write(y_label_right),
        )
        # Title and m-display
        title = Text("Anand Model: Effect of m", font_size=30).to_edge(UP)
        m_display = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.8)
            .next_to(axes_right, UR)
        )
        self.play(Write(title), FadeIn(m_display))

        # Left curve (dot{ep} vs sigma)
        def get_dot_ep_curve():
            m = m_tracker.get_value()
            sigma_vals = np.linspace(0.01, 3, 300)
            dot_eps = A * np.exp(-Q / (R * T)) * np.sinh(xi * sigma_vals / s) ** m
            return axes_left.plot_line_graph(
                x_values=sigma_vals,
                y_values=dot_eps,
                line_color=interpolate_color(RED, BLUE, m / 0.5),
                add_vertex_dots=False,
                stroke_width=4,
            )

        # Right curve (ep vs sigma)
        def get_ep_curve():
            m = m_tracker.get_value()
            sigma_vals = np.linspace(0.01, 3, 300)
            dot_eps = A * np.exp(-Q / (R * T)) * np.sinh(xi * sigma_vals / s) ** m
            eps_vals = np.cumsum(dot_eps) * (sigma_vals[1] - sigma_vals[0])
            return axes_right.plot_line_graph(
                x_values=eps_vals,
                y_values=sigma_vals,
                line_color=interpolate_color(BLUE, RED, m / 0.5),
                add_vertex_dots=False,
                stroke_width=4,
            )

        # Dynamic updates
        dot_ep_curve = always_redraw(get_dot_ep_curve)
        ep_curve = always_redraw(get_ep_curve)
        self.add(dot_ep_curve, ep_curve)
        # Animate m smoothly
        self.play(m_tracker.animate.set_value(0.5), run_time=6, rate_func=linear)
        self.wait()
