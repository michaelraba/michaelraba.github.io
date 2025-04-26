from manim import *
import numpy as np


class AnandFlowDualPlots(Scene):
    def construct(self):
        # Parameters
        A = 1.0
        Q = 1.0
        R = 1.0
        T = 1.0
        s = 1.0
        xi = 1.0
        strain_vals = np.linspace(0.01, 3, 300)
        m_tracker = ValueTracker(0.5)
        # Axes setup
        axes1 = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 10, 2],
            x_length=5.5,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes2 = axes1.copy()
        axes_group = VGroup(axes1, axes2).arrange(RIGHT, buff=1)
        axes1_labels = axes1.get_axis_labels(
            x_label=MathTex(r"\varepsilon^p"), y_label=MathTex(r"\dot{\varepsilon}^p")
        )
        axes2_labels = axes2.get_axis_labels(
            x_label=MathTex(r"\varepsilon^p"), y_label=MathTex(r"\sigma")
        )
        self.play(Create(axes_group), Write(axes1_labels), Write(axes2_labels))

        def get_color(m):
            return interpolate_color(ORANGE, BLUE, (m - 0.01) / (0.5 - 0.01))

        def get_left_curve():
            m = m_tracker.get_value()
            y_vals = A * np.exp(-Q / (R * T)) * np.sinh(xi * strain_vals / s) ** m
            return axes1.plot_line_graph(
                x_values=strain_vals,
                y_values=y_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=3,
            )

        def get_right_curve():
            m = m_tracker.get_value()
            sigma_vals = (
                s * np.arcsinh(strain_vals / A * np.exp(Q / (R * T))) ** (1 / m) / xi
            )
            return axes2.plot_line_graph(
                x_values=strain_vals,
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
        self.play(m_tracker.animate.set_value(0.05), run_time=6)
        self.wait()
