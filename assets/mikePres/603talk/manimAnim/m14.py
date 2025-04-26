from manim import *
import numpy as np


class AnandFlowLaw(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        x_label = axes.get_x_axis_label(Tex(r"$\sigma$"))
        y_label = axes.get_y_axis_label(Tex(r"$\dot{\varepsilon}^p$"))
        title = Text("Anand Flow Law: Varying $m$", font_size=32).to_edge(UP)

        self.play(Create(axes), Write(x_label), Write(y_label), Write(title))

        # Constants
        s = 1.0
        xi = 1.0
        A = 1.0
        x_vals = np.linspace(0.01, 3, 300)

        # Tracker for m
        m_tracker = ValueTracker(0.5)

        # Function to update the curve
        def get_curve():
            m = m_tracker.get_value()
            y_vals = A * np.sinh(xi * x_vals / s) ** m
            return axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                add_vertex_dots=False,
                line_color=interpolate_color(BLUE, RED, (0.5 - m) / 0.5),
            )

        # Always redraw curve
        curve = always_redraw(get_curve)

        # m display
        m_label = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.8)
            .next_to(axes, UR)
        )

        self.add(curve, m_label)

        # Animate m from 0.5 → 0.01
        self.play(m_tracker.animate.set_value(0.01), run_time=6)
        self.wait()
