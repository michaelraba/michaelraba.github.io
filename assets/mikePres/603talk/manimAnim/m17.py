#!/usr/bin/env python3.10

from manim import *
import numpy as np


class AnandDualPlot(Scene):
    def construct(self):
        # Constants
        A = 1.0
        xi = 1.0
        s = 1.0
        x_vals = np.linspace(0.01, 3, 300)
        m_values = np.linspace(0.05, 0.5, 20)
        # Axes for the two plots
        axes_left = (
            Axes(
                x_range=[0, 10, 2],
                y_range=[0, 3, 1],
                x_length=5,
                y_length=4,
                axis_config={"include_numbers": True},
            )
            .to_edge(LEFT)
            .shift(DOWN * 0.5)
        )
        axes_right = (
            Axes(
                x_range=[0, 6, 1],
                y_range=[0, 3, 1],
                x_length=5,
                y_length=4,
                axis_config={"include_numbers": True},
            )
            .to_edge(RIGHT)
            .shift(DOWN * 0.5)
        )
        # Axis labels
        axes_left_labels = (
            axes_left.get_x_axis_label(MathTex(r"\dot{\varepsilon}^p")),
            axes_left.get_y_axis_label(MathTex(r"\sigma")),
        )
        axes_right_labels = (
            axes_right.get_x_axis_label(MathTex(r"\varepsilon^p")),
            axes_right.get_y_axis_label(MathTex(r"\sigma")),
        )
        title = Text("Effect of $m$ in Anand's Model", font_size=28).to_edge(UP)
        self.play(
            Create(axes_left),
            Create(axes_right),
            Write(title),
            Write(axes_left_labels[0]),
            Write(axes_left_labels[1]),
            Write(axes_right_labels[0]),
            Write(axes_right_labels[1]),
        )

        # Function for generating the curves
        def get_graphs(m):
            sigma_vals = x_vals
            ep_dot_vals = A * np.sinh(xi * sigma_vals / s) ** m
            ep_vals = np.cumsum(ep_dot_vals) * (sigma_vals[1] - sigma_vals[0])
            graph_left = axes_left.plot_line_graph(
                x_values=ep_dot_vals,
                y_values=sigma_vals,
                line_color=BLUE,
                add_vertex_dots=False,
                stroke_width=3,
            )
            graph_right = axes_right.plot_line_graph(
                x_values=ep_vals,
                y_values=sigma_vals,
                line_color=RED,
                add_vertex_dots=False,
                stroke_width=3,
            )
            return VGroup(graph_left, graph_right)

        # Animate each m
        for m in m_values:
            label = MathTex(f"m = {m:.2f}").scale(0.8).next_to(title, DOWN)
            grp = get_graphs(m)
            self.play(Create(grp), Write(label), run_time=0.4)
            self.remove(grp, label)
        # Final frame
        final_m = m_values[-1]
        final_grp = get_graphs(final_m)
        final_label = MathTex(f"m = {final_m:.2f}").scale(0.8).next_to(title, DOWN)
        self.play(Create(final_grp), Write(final_label))
        self.wait(2)
