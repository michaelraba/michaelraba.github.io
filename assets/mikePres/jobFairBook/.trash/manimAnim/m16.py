#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandFlowAndAccumulatedStrain(Scene):
    def construct(self):
        # Axes setup
        axes1 = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT)
        axes2 = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 12, 2],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT)
        x_label1 = axes1.get_x_axis_label(Tex(r"$\sigma$"))
        y_label1 = axes1.get_y_axis_label(Tex(r"$\dot{\varepsilon}^p$"))
        title1 = Text("Flow Law", font_size=24).next_to(axes1, UP)
        x_label2 = axes2.get_x_axis_label(Tex(r"$\sigma$"))
        y_label2 = axes2.get_y_axis_label(Tex(r"$\varepsilon^p$"))
        title2 = Text("Accumulated Strain", font_size=24).next_to(axes2, UP)
        self.play(
            Create(axes1),
            Create(axes2),
            Write(x_label1),
            Write(y_label1),
            Write(title1),
            Write(x_label2),
            Write(y_label2),
            Write(title2),
        )
        # Constants
        s = 1.0
        xi = 1.0
        A = 1.0
        x_vals = np.linspace(0.01, 3, 300)
        dt = 1.0  # time step
        # Tracker for m
        m_tracker = ValueTracker(0.5)

        def get_color(m):
            return interpolate_color(ORANGE, BLUE, (0.5 - m) / 0.5)

        def get_flow_curve():
            m = m_tracker.get_value()
            y_vals = A * np.sinh(xi * x_vals / s) ** m
            return axes1.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=4,
            )

        def get_strain_curve():
            m = m_tracker.get_value()
            y_vals = A * np.sinh(xi * x_vals / s) ** m
            ep_vals = np.cumsum(y_vals) * (x_vals[1] - x_vals[0]) * dt
            return axes2.plot_line_graph(
                x_values=x_vals,
                y_values=ep_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=4,
            )

        # Always redraw both plots
        flow_curve = always_redraw(get_flow_curve)
        strain_curve = always_redraw(get_strain_curve)
        m_label = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}").scale(0.8).to_corner(UL)
        )
        self.add(flow_curve, strain_curve, m_label)
        self.play(m_tracker.animate.set_value(0.01), run_time=6)
        self.wait()
