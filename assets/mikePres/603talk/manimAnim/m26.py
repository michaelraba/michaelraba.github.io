#!/usr/bin/env python3.10

from manim import *
import numpy as np

class AnandSigmaVsEpsDotDiscrete(Scene):
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

        # Define eps_dot values (x axis)
        eps_dot_vals = np.linspace(1e2, 2e4, 300)

        # m values to show (discrete, clean)
        m_vals = [0.005, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]

        # Initialize empty references
        current_curve = None
        current_label = None

        for m in m_vals:
            sigma_vals = []
            for eps_dot in eps_dot_vals:
                sinh_inv_arg = (eps_dot / (A * exp_factor)) ** m
                sigma = (np.arcsinh(sinh_inv_arg)) * s / j
                sigma_vals.append(sigma)

            new_curve = axes1.plot_line_graph(
                x_values=eps_dot_vals,
                y_values=sigma_vals,
                add_vertex_dots=False,
                line_color=interpolate_color(ORANGE, BLUE, (m - 0.005) / (1.0 - 0.005)),
                stroke_width=4,
            )

            new_label = MathTex(f"m = {m:.3f}").scale(0.8).to_corner(UL)

            animations = []
            if current_curve:
                animations.append(FadeOut(current_curve))
            if current_label:
                animations.append(FadeOut(current_label))
            animations.append(FadeIn(new_curve))
            animations.append(FadeIn(new_label))

            self.play(*animations, run_time=1.5)

            current_curve = new_curve
            current_label = new_label

        self.wait()

