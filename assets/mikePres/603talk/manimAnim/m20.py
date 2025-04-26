#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandStrainBasedGraphs(Scene):
    def construct(self):
        A = 1.0
        Q = 1.0
        R = 1.0
        T = 1.0
        xi = 1.0
        s = 1.0
        m_tracker = ValueTracker(0.05)
        axes_left = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes_right = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes_group = VGroup(axes_left, axes_right).arrange(RIGHT, buff=1).to_edge(DOWN)
        self.play(Create(axes_group))
        x_label = MathTex(r"\varepsilon^p")
        y_label_left = MathTex(r"\dot{\varepsilon}^p")
        y_label_right = MathTex(r"\sigma")
        self.play(
            Write(axes_left.get_x_axis_label(x_label)),
            Write(axes_left.get_y_axis_label(y_label_left)),
            Write(axes_right.get_x_axis_label(x_label.copy())),
            Write(axes_right.get_y_axis_label(y_label_right)),
        )
        title = Text("Anand Model: Effect of m", font_size=36).to_edge(UP)
        m_display = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.9)
            .next_to(axes_right, UP, buff=0.3)
        )
        self.play(Write(title), FadeIn(m_display))

        def get_dot_ep_curve():
            m = m_tracker.get_value()
            ep = np.linspace(0.01, 6, 300)
            sigma = ep
            dot_ep = A * np.exp(-Q / (R * T)) * np.sinh(xi * sigma / s) ** m
            return axes_left.plot_line_graph(
                x_values=ep,
                y_values=dot_ep,
                line_color=interpolate_color(RED, BLUE, m / 0.5),
                stroke_width=4,
            )

        def get_sigma_curve():
            ep = np.linspace(0.01, 6, 300)
            sigma = ep
            return axes_right.plot_line_graph(
                x_values=ep,
                y_values=sigma,
                line_color=interpolate_color(BLUE, RED, m_tracker.get_value() / 0.5),
                stroke_width=4,
            )

        dot_ep_curve = always_redraw(get_dot_ep_curve)
        sigma_curve = always_redraw(get_sigma_curve)
        self.add(dot_ep_curve, sigma_curve)
        self.play(m_tracker.animate.set_value(0.5), run_time=6, rate_func=linear)
        self.wait()
