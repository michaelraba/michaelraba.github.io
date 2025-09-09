# Refactored Manim Animation: Anand's Model Constitutive Flow
from manim import *


class AnandConstitutiveFlow(Scene):
    def construct(self):
        slides = []

        # Slide 1: Intro to Flow
        intro_title = Text("Constitutive Flow of Anand's Model", font_size=40).to_edge(
            UP
        )
        flow_items = (
            VGroup(
                Text("(I) Start in Current Configuration", font_size=28),
                Text("(II) Pull Back to Reference Configuration", font_size=28),
                Text("(III) Apply Thermodynamic Assumptions (i)-(iv)", font_size=28),
                Text("(IV) Simplify via Assumptions (a1)-(a5)", font_size=28),
                Text("(V) Rotate to Current Frame", font_size=28),
                Text("(VI) Final Engineering Model (Eqs. 77-86)", font_size=28),
            )
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .scale(0.9)
            .next_to(intro_title, DOWN, buff=0.8)
        )
        self.play(Write(intro_title), FadeIn(flow_items))
        self.wait(4)
        self.play(FadeOut(intro_title), FadeOut(flow_items))

        # Slide 2: Start in Current Config
        t1 = Text("(I) Current Configuration: Basic Setup", font_size=36).to_edge(UP)
        eqs1 = (
            VGroup(
                MathTex(r"\mathbf{T}, \mathbf{L} = \mathbf{L}^e + \mathbf{L}^p"),
                MathTex(r"\psi = \psi(\theta, \mathbf{T})"),
                MathTex(r"\dot{\omega} = \rho^{-1} \mathbf{T} : \mathbf{L}"),
            )
            .arrange(DOWN)
            .scale(0.9)
            .shift(UP * 0.5)
        )
        lbl1 = Text(
            "Stress, strain rate, and dissipation in current configuration",
            font_size=26,
        ).next_to(eqs1, DOWN)
        self.play(Write(t1), Write(eqs1), FadeIn(lbl1))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 3: Pull Back to Reference Config
        t2 = Text("(II) Pull Back to Reference Configuration", font_size=36).to_edge(UP)
        eqs2 = (
            VGroup(
                MathTex(r"\tilde{\mathbf{T}} = \det \mathbf{F} \cdot \mathbf{T}"),
                MathTex(
                    r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p, \quad \det \mathbf{F}^p = 1"
                ),
                MathTex(
                    r"\dot{\phi}_r + \eta_r \dot{\theta} + \mathbf{E}^e : \dot{\tilde{\mathbf{T}}} - (\mathbf{C}^T \tilde{\mathbf{T}}) : \mathbf{L}^p + \theta \dot{s} \leq 0"
                ),
            )
            .arrange(DOWN)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        lbl2 = Text("Reduced Dissipation Inequality (Eq. 28)", font_size=26).next_to(
            eqs2, DOWN
        )
        self.play(Write(t2), Write(eqs2), FadeIn(lbl2))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 4: Seven Smooth Response Functions
        t3 = Text("Constitutive Structure: 7 Response Functions", font_size=36).to_edge(
            UP
        )
        eqs3 = (
            VGroup(
                MathTex(
                    r"\dot{\phi}_r = \hat{\phi}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\eta_r = \hat{\eta}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\mathbf{E}^e = \hat{\mathbf{E}}^e(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\dot{\mathbf{q}} = \hat{\mathbf{q}}(\tilde{\mathbf{T}}, \theta, \mathbf{g}, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\mathbf{L}^p = \hat{\mathbf{G}}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\dot{\mathbf{B}} = \hat{\mathbf{B}}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\dot{s} = \hat{s}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
            )
            .arrange(DOWN)
            .scale(0.75)
            .shift(UP * 0.2)
        )
        self.play(Write(t3), Write(eqs3))
        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 5: Simplifying Assumptions (Z4)
        t4 = Text("(III) Apply Thermodynamic Constraints (Z4)", font_size=36).to_edge(
            UP
        )
        eqs4 = (
            VGroup(
                MathTex(r"\mathbf{D}^p = x_1 \tilde{\mathbf{T}}'"),
                MathTex(
                    r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}"
                ),
                MathTex(
                    r"\dot{s} = \hat{s}(l), \quad l = \{ \tau, \bar{\tau}_b, s, \theta, \bar{p} \}"
                ),
            )
            .arrange(DOWN)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        lbl4 = Text(
            "Using isotropy, incompressibility, and frame indifference", font_size=26
        ).next_to(eqs4, DOWN)
        self.play(Write(t4), Write(eqs4), FadeIn(lbl4))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 6: Push Forward to Current Config
        t5 = Text("(IV) Rotate to Current Configuration", font_size=36).to_edge(UP)
        eqs5 = (
            MathTex(
                r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}, \quad \mathbf{D}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}"
            )
            .scale(0.85)
            .shift(DOWN * 0.5)
        )
        lbl5 = Text("Jaumann Derivatives & Frame Transformation", font_size=26).next_to(
            eqs5, DOWN
        )
        self.play(Write(t5), Write(eqs5), FadeIn(lbl5))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Slide 7: Final Model (Eqs. 77–86)
        t6 = Text("(V) Final Practical Model for FEA", font_size=36).to_edge(UP)
        eqs6 = (
            VGroup(
                MathTex(
                    r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \Pi \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{D}^p = \dot{\gamma}^p \left\{ \frac{\tilde{\mathbf{T}}'}{2 \bar{\tau}} \right\}"
                ),
                MathTex(
                    r"\dot{s} = h(\bar{\tau}, s, \theta) \dot{\gamma}^p - r(s, \theta)"
                ),
                MathTex(
                    r"\bar{\tau} = \left\{ \frac{1}{2} \text{tr}(\tilde{\mathbf{T}}'^2) \right\}^{1/2}"
                ),
            )
            .arrange(DOWN)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        lbl6 = Text(
            "Used for Backward Euler Integration & Parametric Fit", font_size=26
        ).next_to(eqs6, DOWN)
        self.play(Write(t6), Write(eqs6), FadeIn(lbl6))
        self.wait(5)
