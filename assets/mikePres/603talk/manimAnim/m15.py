from manim import *
import numpy as np


class AnandFlowLog(Scene):
    def construct(self):
        # Axes with "fake" log scale on y-axis
        axes = Axes(
            x_range=[0, 1.5, 0.25],
            y_range=[-2, 1.5, 1],  # log10 scale: 10^-2 to 10^1
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        x_label = axes.get_x_axis_label(Tex(r"$\sigma$"))
        y_label = axes.get_y_axis_label(Tex(r"$\log_{10} \dot{\varepsilon}^p$"))
        title = Text("Effect of $m$ in Anand's Model", font_size=32).to_edge(UP)

        self.play(Create(axes), Write(x_label), Write(y_label), Write(title))

        # Constants (arbitrary but illustrative)
        s = 1.0
        xi = 1.0
        A = 1.0
        x_vals = np.linspace(0.01, 1.5, 400)

        # Tracker for m
        m_tracker = ValueTracker(1.0)

        # Color gradient: orange → pink → blue
        def get_color(m):
            # return color_gradient([ORANGE, PINK, BLUE], 10)[int(m * 10)]
            return color_gradient([ORANGE, PINK, BLUE], 10)[min(int(m * 10), 9)]

        # Function to update the curve
        def get_curve():
            m = m_tracker.get_value()
            y_vals = A * np.sinh(xi * x_vals / s) ** m
            y_vals = np.log10(y_vals)
            return axes.plot_line_graph(
                x_values=x_vals,
                y_values=y_vals,
                add_vertex_dots=False,
                line_color=get_color(m),
                stroke_width=4,
            )

        # Always redraw curve
        curve = always_redraw(get_curve)

        # m display
        m_label = always_redraw(
            lambda: MathTex(f"m = {m_tracker.get_value():.2f}")
            .scale(0.9)
            .next_to(axes, UR)
        )

        self.add(curve, m_label)

        # Animate m from 1 → 0.01
        self.play(m_tracker.animate.set_value(0.01), run_time=6)
        self.wait()
