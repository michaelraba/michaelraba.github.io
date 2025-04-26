# Animated Evolution of a Single Equation in Anand's Model
from manim import *


class AnandConstitutiveEvolution(MovingCameraScene):
    def construct(self):
        title = Text("Constitutive Evolution in Anand Model", font_size=36).to_edge(UP)
        self.play(FadeIn(title))

        # Step 1: Initial definition in current configuration
        eq1 = MathTex(
            r"\dot{\omega} = \frac{\rho_0}{\rho} \mathbf{T} : \mathbf{L}", font_size=36
        )
        label1 = Text("Power of internal forces", font_size=24).next_to(eq1, DOWN)
        self.play(Write(eq1), FadeIn(label1))
        self.wait(2)

        # Step 2: Replace T and pull back to reference configuration
        eq2 = MathTex(
            r"\dot{\phi}_r = \hat{\phi}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)",
            font_size=36,
        ).next_to(eq1, DOWN * 2.5)
        label2 = Text(
            "Thermodynamic form, reference config (Eq. 28)", font_size=24
        ).next_to(eq2, DOWN)
        self.play(TransformFromCopy(eq1, eq2), FadeIn(label2))
        self.wait(2)

        # Step 3: Thermodynamic condition application
        eq3 = MathTex(
            r"\dot{\mathbf{E}}^e = \mathbb{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}",
            font_size=36,
        ).next_to(eq2, DOWN * 2.5)
        label3 = Text(
            "Constitutive form via thermodynamic constraints", font_size=24
        ).next_to(eq3, DOWN)
        self.play(Write(eq3), FadeIn(label3))
        self.wait(2)

        # Step 4: Simplification through assumptions
        eq4 = MathTex(
            r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1(\tilde{\mathbf{T}}'\mathbf{B} - \mathbf{B}\tilde{\mathbf{T}}')",
            font_size=36,
        ).next_to(eq3, DOWN * 2.5)
        label4 = Text("Flow rule form after assumptions (a1–a6)", font_size=24).next_to(
            eq4, DOWN
        )
        self.play(Write(eq4), FadeIn(label4))
        self.wait(2)

        # Step 5: Rotation to current configuration
        eq5 = MathTex(
            r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}",
            font_size=36,
        ).next_to(eq4, DOWN * 2.5)
        label5 = Text("Final Jaumann rate form (Eq. 77)", font_size=24).next_to(
            eq5, DOWN
        )
        self.play(Write(eq5), FadeIn(label5))
        self.wait(3)

        # Final zoom-out
        all_eqs = VGroup(
            title, eq1, label1, eq2, label2, eq3, label3, eq4, label4, eq5, label5
        )
        self.play(self.camera.frame.animate.scale(1.3).move_to(all_eqs))
        self.wait(2)
