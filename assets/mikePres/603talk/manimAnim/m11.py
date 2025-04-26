#!/usr/bin/env python3.10

# Full Derivation of Anand's Constitutive Model (Expanded Version)
from manim import *


class AnandFullProcedure(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(0.8)
        title = Text(
            "Anand (1985): Full Thermo-Viscoplastic Model Derivation", font_size=34
        ).to_edge(UP)
        self.play(FadeIn(title))

        slide_counter = 1

        def slide(equation, label_text, color=None):
            nonlocal slide_counter
            label = Text(f"{slide_counter}. {label_text}", font_size=26).next_to(
                equation, DOWN
            )
            self.play(Write(equation), FadeIn(label))
            if color:
                self.play(equation.animate.set_color(color))
            self.wait(2)
            slide_counter += 1

        # Slide 1: Kinematic decomposition
        eq1 = MathTex(
            r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p, \quad \det \mathbf{F}^p = 1",
            font_size=34,
        )
        slide(eq1, "Kinematic decomposition of deformation gradient", color=BLUE)

        # Slide 2: State variables
        eq2 = MathTex(
            r"\{ \mathbf{F}^e, \theta, \mathbf{g}, \bar{\mathbf{B}}, s \}", font_size=34
        )
        slide(eq2, "State variables of the system", color=ORANGE)

        # Slide 3: Energy balance
        eq3 = MathTex(
            r"\dot{\phi}_r = \rho \dot{\psi} - \mathbf{T} : \dot{\mathbf{E}}^e - \eta_r \dot{\theta}",
            font_size=34,
        )
        slide(eq3, "Energy balance decomposition", color=GREEN)

        # Slide 4: Entropy relation
        eq4 = MathTex(r"\eta_r = -\frac{\partial \psi}{\partial \theta}", font_size=34)
        slide(eq4, "Entropy defined from free energy", color=YELLOW)

        # Slide 5: Reduced dissipation inequality
        eq5 = MathTex(
            r"\mathbf{T} : \mathbf{L}^p - \dot{\psi} + \eta_r \dot{\theta} \geq 0",
            font_size=34,
        )
        slide(eq5, "Reduced dissipation inequality (Eq. 28)", color=RED)

        # Slide 6: Pull-back to reference configuration
        eq6 = MathTex(
            r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}, \quad \mathbf{D} = \mathbf{R}^T \dot{\mathbf{E}}^e \mathbf{R}",
            font_size=34,
        )
        slide(eq6, "Rotate variables to reference configuration")

        # Slide 7: General constitutive forms
        eq7 = MathTex(
            r"\dot{\mathbf{E}}^e = \hat{\mathbf{K}} + \hat{\mathbf{A}} \dot{\theta}, \quad \dot{s} = \hat{s}()",
            font_size=34,
        )
        slide(eq7, "General thermodynamic constitutive response functions", color=BLUE)

        # Slide 8: Polynomial simplification of flow rule
        eq8 = MathTex(
            r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1(\tilde{\mathbf{T}}' \mathbf{B} - \mathbf{B} \tilde{\mathbf{T}}')",
            font_size=34,
        )
        slide(eq8, "Simplified polynomial form for flow (Eq. 60)", color=GREEN)

        # Slide 9: Evolution of s
        eq9 = MathTex(
            r"\dot{s} = h_0 \left| 1 - \frac{s}{s^*} \right|^a \text{sign}\left(1 - \frac{s}{s^*} \right) \dot{\bar{\varepsilon}}^p",
            font_size=32,
        )
        slide(eq9, "Evolution equation of internal scalar s (Eq. 63)", color=RED)

        # Slide 10: Push forward to current configuration
        eq10 = MathTex(
            r"\mathbf{L}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}, \quad \tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}",
            font_size=34,
        )
        slide(eq10, "Push tensors back to spatial frame")

        # Slide 11: Final simplified FEA-ready form
        eq11 = MathTex(
            r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}",
            font_size=34,
        )
        slide(eq11, "Stress rate equation (Eq. 77)", color=PURPLE)

        eq12 = MathTex(
            r"\mathbf{D}^p = \dot{\bar{\varepsilon}}^p \left\{ \frac{\tilde{\mathbf{T}}'}{2\bar{\tau}} \right\}",
            font_size=34,
        ).next_to(eq11, DOWN * 2)
        self.play(Write(eq12))
        self.wait(2)

        eq13 = MathTex(
            r"\dot{s} = h(\bar{\sigma}, s, \theta) \dot{\bar{\varepsilon}}^p - r(s, \theta)",
            font_size=34,
        ).next_to(eq12, DOWN * 2)
        self.play(Write(eq13))
        self.wait(3)

        # Final zoom-out
        all_eqs = VGroup(
            title, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13
        )
        self.play(self.camera.frame.animate.scale(1.2).move_to(all_eqs))
        self.wait(2)
