#!/usr/bin/env python3.10

from manim import *


class AnandEquationFlow(MovingCameraScene):
    def construct(self):
        # Title
        title = Text(
            "Anand Model: Evolution of a Constitutive Equation", font_size=36
        ).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        # Step 1: Original Form in Mixed Config
        eq1 = MathTex(
            r"\dot{\omega} = \frac{\rho_0}{\rho} \mathbf{T} : \mathbf{L}", font_size=36
        ).shift(UP * 2)
        label1 = Text("Current Configuration", font_size=24).next_to(eq1, DOWN)
        self.play(Write(eq1), FadeIn(label1))
        self.wait(1.5)

        # Step 2: Pull back to Reference Config
        arrow1 = Arrow(eq1.get_bottom(), eq1.get_bottom() + DOWN * 1.5, buff=0.1)
        self.play(GrowArrow(arrow1))
        eq2 = MathTex(
            r"\dot{\phi}_r = \hat{\phi}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)",
            font_size=36,
        ).next_to(arrow1, DOWN, buff=0.5)
        label2 = Text("Reference Configuration (Eq. 28)", font_size=24).next_to(
            eq2, DOWN
        )
        self.play(TransformFromCopy(eq1, eq2), FadeIn(label2))
        self.wait(1.5)

        # Step 3: Apply Thermo Constraints
        arrow2 = Arrow(eq2.get_bottom(), eq2.get_bottom() + DOWN * 1.5, buff=0.1)
        self.play(GrowArrow(arrow2))
        eq3 = MathTex(
            r"\dot{\mathbf{E}}^e = \mathbf{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}",
            font_size=36,
        ).next_to(arrow2, DOWN, buff=0.5)
        label3 = Text("Constitutive Form via Thermo Assumptions", font_size=24).next_to(
            eq3, DOWN
        )
        self.play(Write(eq3), FadeIn(label3))
        self.wait(1.5)

        # Step 4: Rotate to Current Configuration
        arrow3 = Arrow(eq3.get_bottom(), eq3.get_bottom() + DOWN * 1.5, buff=0.1)
        self.play(GrowArrow(arrow3))
        eq4 = MathTex(
            r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}",
            font_size=36,
        ).next_to(arrow3, DOWN, buff=0.5)
        label4 = Text("Push Forward to Current Config (Eq. 77)", font_size=24).next_to(
            eq4, DOWN
        )
        self.play(Write(eq4), FadeIn(label4))
        self.wait(2)

        # Final frame zoom out to show all steps
        full_frame = VGroup(
            title,
            eq1,
            label1,
            arrow1,
            eq2,
            label2,
            arrow2,
            eq3,
            label3,
            arrow3,
            eq4,
            label4,
        )
        self.play(self.camera.frame.animate.scale(1.3).move_to(full_frame))
        self.wait(2)
