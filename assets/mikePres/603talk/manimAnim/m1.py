from manim import *


class ConstitutiveEquationEvolutions(Scene):
    def construct(self):
        title = Text(
            "Evolution of Constitutive Equations in Anand's Model", font_size=36
        ).to_edge(UP)

        # Frame 1: Initial Kinematics
        eq1 = MathTex(
            r"\mathbf{F} = \frac{\partial \vec{\mathbf{x}}(\mathbf{p}, t)}{\partial \mathbf{p}}",
            r"\quad \mathbf{L} = \dot{\mathbf{F}} \mathbf{F}^{-1}",
            font_size=36,
        )
        label1 = Text("Kinematic Definitions", font_size=30).next_to(eq1, DOWN)

        # Frame 2: Decomposition
        eq2 = MathTex(
            r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p",
            r"\quad \mathbf{L} = \mathbf{L}^e + \mathbf{L}^p",
            font_size=36,
        )
        eq2[0][2:7].set_color(ORANGE)  # Highlight F^e F^p
        label2 = Text("Multiplicative Decomposition", font_size=30).next_to(eq2, DOWN)

        # Frame 3: Replace state vars
        eq3 = MathTex(
            r"\{ \mathbf{F}, \theta, \mathbf{g}, \mathbf{F}^p, \mathbf{B}, s \}",
            font_size=36,
        )
        eq3_new = MathTex(
            r"\{ \mathbf{F}^e, \theta, \mathbf{g}, \mathbf{B}, s \}", font_size=36
        )
        eq3[0][2:11].set_color(RED)  # highlight F^p
        eq3_new[0][2:6].set_color(GREEN)
        label3 = Text("Replace F, F^p with F^e", font_size=30).next_to(eq3_new, DOWN)

        # Frame 4: Replace E^e with T̃
        eq4_old = MathTex(
            r"\dot{\omega} = \tilde{\mathbf{T}} : \dot{\mathbf{E}}^e + ( \mathbf{C}^e \tilde{\mathbf{T}} ) : \mathbf{L}^p",
            font_size=34,
        )
        eq4_new = MathTex(
            r"\dot{\omega} = \mathbb{K}[\tilde{\mathbf{T}}] : \tilde{\mathbf{T}} + \cdots",
            font_size=34,
        )
        eq4_old[0][22:35].set_color(RED)
        eq4_new[0][0:17].set_color(GREEN)
        label4 = Text("Replace E^e using K[T̃]", font_size=30).next_to(eq4_new, DOWN)

        # Frame 5: Final constitutive laws
        eq5 = MathTex(
            r"\dot{\mathbf{E}}^e = \mathbb{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}",
            r"\quad \mathbf{L}^p = x_1 \tilde{\mathbf{T}} + \eta_1 (\tilde{\mathbf{B}} - \mathbf{B} \tilde{\mathbf{T}})",
            font_size=30,
        )
        label5 = Text("Final Constitutive Equations", font_size=30).next_to(eq5, DOWN)

        # Display each transformation with fade
        self.play(FadeIn(title))
        self.wait(0.5)

        self.play(Write(eq1), FadeIn(label1))
        self.wait(2)
        self.play(FadeOut(eq1), FadeOut(label1))

        self.play(Write(eq2), FadeIn(label2))
        self.wait(2)
        self.play(FadeOut(eq2), FadeOut(label2))

        self.play(Write(eq3))
        self.wait(1)
        self.play(Transform(eq3, eq3_new), FadeIn(label3))
        self.wait(2)
        self.play(FadeOut(eq3), FadeOut(label3))

        self.play(Write(eq4_old))
        self.wait(1)
        self.play(Transform(eq4_old, eq4_new), FadeIn(label4))
        self.wait(2)
        self.play(FadeOut(eq4_old), FadeOut(label4))

        self.play(Write(eq5), FadeIn(label5))
        self.wait(3)
        self.play(FadeOut(eq5), FadeOut(label5), FadeOut(title))
