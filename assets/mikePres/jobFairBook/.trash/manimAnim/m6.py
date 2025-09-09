#!/usr/bin/env python3.10

from manim import *


class AnandModelWithSteps(Scene):
    def construct(self):
        def slide(title_text, eqs, label_text=None, wait_time=2.5):
            title = Text(title_text, font_size=36).to_edge(UP)
            body = VGroup(
                *[
                    MathTex(eq).scale(0.85).to_edge(LEFT).shift(DOWN * i * 0.9)
                    for i, eq in enumerate(eqs)
                ]
            )
            label = (
                Text(label_text, font_size=28).next_to(body, DOWN)
                if label_text
                else None
            )

            self.play(FadeIn(title))
            for eq in body:
                self.play(Write(eq))
            if label:
                self.play(FadeIn(label))
            self.wait(wait_time)
            self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 1: Start in current configuration
        slide(
            "Start: Current Configuration",
            [
                r"\mathbf{L} = \dot{\mathbf{F}} \mathbf{F}^{-1} = \mathbf{L}^e + \mathbf{L}^p",
                r"\dot{\omega} = \frac{\rho_0}{\rho} \mathbf{T} : \mathbf{L}",
                r"\phi_r = \rho \psi - \mathbf{T} : \mathbf{E}^e",
            ],
            "Stress power & free energy terms",
        )

        # Slide 2: Pull back to reference configuration
        slide(
            "Pull Back to Reference Configuration",
            [
                r"\mathbf{T} \rightarrow \tilde{\mathbf{T}} = \det(\mathbf{F}) \mathbf{T}",
                r"\dot{\phi}_r = \hat{\phi}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)",
                r"\eta_r = -\frac{\partial \hat{\phi}}{\partial \theta}",
            ],
            "Reduced dissipation inequality: Eq. (28)",
        )

        # Slide 3: Apply Thermodynamic Constraints (i–iv)
        slide(
            "Thermodynamic Restrictions",
            [
                r"\dot{\mathbf{E}}^e = -\frac{\partial \hat{\phi}}{\partial \tilde{\mathbf{T}}}",
                r"\eta_r = -\frac{\partial \hat{\phi}}{\partial \theta}",
                r"(C^e \tilde{\mathbf{T}}) : \mathbf{L}^p - \frac{\partial \hat{\phi}}{\partial \mathbf{B}} : \dot{\mathbf{B}} - \frac{\partial \hat{\phi}}{\partial s} \dot{s} \ge 0",
            ],
            "Thermodynamic identities",
        )

        # Slide 4: Insert Scalar Quantities
        slide(
            "Simplify Using Scalars",
            [
                r"\tau = \left\{ \frac{1}{2} \text{tr}(\tilde{\mathbf{T}}'^2) \right\}^{1/2}",
                r"\bar{p} = -\frac{1}{3} \text{tr}(\tilde{\mathbf{T}})",
                r"\bar{\tau}_b = \left\{ \frac{1}{2} \text{tr}(\mathbf{B}^2) \right\}^{1/2}",
            ],
            "Effective stress and invariants",
        )

        # Slide 5: Functional Forms of Constitutive Laws
        slide(
            "Functional Forms from Assumptions",
            [
                r"\dot{\mathbf{E}}^e = \mathbb{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}",
                r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1 (\tilde{\mathbf{T}}' \mathbf{B} - \mathbf{B} \tilde{\mathbf{T}}')",
                r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}",
            ],
            "Simplified model under (a1)–(a6)",
        )

        # Slide 6: Rotate to current configuration
        slide(
            "Rotation to Current Configuration",
            [
                r"\dot{\mathbf{E}}^e = \mathbf{R}^T \mathbf{D}^e \mathbf{R}",
                r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}",
                r"\mathbf{L}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}",
            ],
            "Apply spin decomposition (Jaumann frame)",
        )

        # Slide 7: Final Simplified Engineering Form
        slide(
            "Final Form (Current Configuration)",
            [
                r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}",
                r"\mathbf{D}^p = \dot{\gamma}^p \left\{ \frac{\tilde{\mathbf{T}}'}{2 \bar{\tau}} \right\}",
                r"\dot{s} = h(\bar{\tau}, s, \theta) \dot{\gamma}^p - r(s, \theta)",
            ],
            "Equations (77)–(86) for implementation",
        )
