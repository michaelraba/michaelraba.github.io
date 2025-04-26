#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandFlowSigmaEpsDotVsSigmaEps(Scene):
    def construct(self):
        # Constants
        A = 1.0
        Q = 1.0
        R = 1.0
        T = 1.0
        s = 1.0
        xi = 1.0
        m_start = 0.5
        m_end = 0.05
        # Strain rate and strain values
        eps_dot_vals = np.linspace(0.01, 10, 300)
        eps_p_vals = np.linspace(0.01, 3, 300)
        # Axes Setup (Left: sigma vs eps_dot, Right: sigma vs eps_p)
        axes1 = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes2 = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes_group = VGroup(axes1, axes2).arrange(RIGHT, buff=1.2)
        axes1_labels = axes1.get_axis_labels(
            x_label=MathTex(r"\dot{\varepsilon}^p"), y_label=MathTex(r"\sigma")
        )
        axes2_labels = axes2.get_axis_labels(
            x_label=MathTex(r"\varepsilon^p"), y_label=MathTex(r"\sigma")
        )
        self.play(Create(axes_group), Write(axes1_labels), Write(axes2_labels))
        # m Tracker
        m_tracker = ValueTracker(m_start)

        def get_color(m):
            return interpolate_color(ORANGE, BLUE, (m - m_end) / (m_start - m_end))

        # Left plot: sigma vs eps_dot
        def get_left_curve():
            m = m_tracker.get_value()
            sigma_vals = (
                s * np.arcsinh(eps_dot_vals / A * np.exp(Q / (R * T))) ** (1 / m) / xi
            )
            return axes1.plot_line_graph(
                x_values=eps_dot_vals,
                y_values=sigma_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=3,
            )

        # Right plot: sigma vs eps_p
        def get_right_curve():
            m = m_tracker.get_value()
            sigma_vals = (
                s * np.arcsinh(eps_p_vals / A * np.exp(Q / (R * T))) ** (1 / m) / xi
            )
            return axes2.plot_line_graph(
                x_values=eps_p_vals,
                y_values=sigma_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=3,
            )

        left_curve = always_redraw(get_left_curve)
        right_curve = always_redraw(get_right_curve)
        m_label = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.8)
            .next_to(axes_group, UP)
        )
        self.add(left_curve, right_curve, m_label)
        self.play(m_tracker.animate.set_value(m_end), run_time=6)
        self.wait()
